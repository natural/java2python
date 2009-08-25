#!/usr/bin/env python
# -*- coding: utf-8 -*-
from cStringIO import StringIO
from logging import info, warn
from re import sub as rxsub
from string import Template

from java2python import expression, maybeAttr
from java2python.config import Config


passLine = [expression(left='pass', right='', format='$left'), ]


class Block:
    """ Base class for blocks of Python source code.

    """
    config = None

    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.lines = []
        self.modifiers = []
        self.preamble = []
        self.epilogue = []
        self.variables = []

    def __iter__(self):
        for line in self.lines:
            yield line

    def dump(self, output, indent):
        """ dump(output, indent) -> write the contents of this block to output

        """
        offset = self.offset(indent)
        for item in self:
            if hasattr(item, 'dump'):
                item.dump(output, indent)
            else:
                item = self.formatExpression(item)
                output.write('%s%s\n' % (offset, item))

    def asString(self):
        """ asString() -> source code defined in obj

        """
        out = StringIO()
        self.dump(out, 0)
        source = out.getvalue()
        for subs in self.config.all('outputSubs', []):
            for sub in subs:
                source = rxsub(sub[0], sub[1], source)
        return source

    def setConfigs(self, configs):
        """ sets the config on the root class so all instances share it

        """
        Block.config = Config(configs)


    def offset(self, indent):
        """ calculated indentation string

        @param indent integer indentation level
        @return string of spaces
        """
        return self.config.last('leadingIndent', '    ') * indent

    def formatExpression(self, value):
        if isinstance(value, (dict, )):
            inner = value.copy()
            format = inner['format']
            if 'right' in value:
                inner['right'] = self.formatExpression(value['right'])
            if 'left' in value:
                inner['left'] = self.formatExpression(value['left'])
            if 'id' in value:
                inner['id'] = self.formatExpression(value['id'])
            value = Template(format).substitute(inner)
        return value

    def append(self, value):
        if self.lines == passLine:
            self.lines.pop()
        if isinstance(value, (basestring, )):
            value = expression(left=value, right='', format='$left')
        self.lines.append(value)

    def insert(self, index, value):
        if self.lines == passLine:
            self.lines.pop()
        if isinstance(value, (basestring, )):
            value = expression(left=value, right='', format='$left')
        self.lines.insert(index, value)


    def setModifiers(self, modifiers):
        self.modifiers.extend(modifiers)


    def dumpConfigValues(self, output, name):
        """ writes a sequence of lines given a config attribute name

        Lines may be callable.  Refer to the config.default module for
        details.

        @param output writable file-like object
        @param name configuration module attribute
        @return None
        """
        for lines in self.config.all(name, []):
            for line in lines:
                line = line(self) if callable(line) else line
                output.write('%s\n' % (line, ))

    def addComment(self, value, index=0, prefix='#'):
        prefix = self.config.last('commentPrefix', prefix)
        ## don't use self.append so that empty blocks don't have
        ## their pass statement popped
        self.lines.append(expression(left=prefix, right=value, format='$left $right'))


    def decl(self):
        return ''

    @property
    def blockHandlers(self):
        return []

    @property
    def methods(self):
        return [block for block in self if maybeAttr(block, 'isMethod')]
