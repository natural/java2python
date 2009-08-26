#!/usr/bin/env python
# -*- coding: utf-8 -*-
from cStringIO import StringIO
from logging import debug, info, warn
from re import sub as rxsub
from string import Template

from java2python import expression, maybeAttr
from java2python.config import Config


passLine = [expression(left='pass', right='', format='$left')]


class Block:
    """ Base class for blocks of (soon-to-be) Python source code.

    """
    config = None

    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.blocks = []
        self.modifiers = []
        self.preamble = []
        self.epilogue = []
        self.variables = []

    def __iter__(self):
        """ to iterate over a block is to iterate over it's blocks """
        for item in self.blocks:
            yield item

    def __len__(self):
        """ returns the length of this block """
        return len(self.blocks)

    def append(self, value):
        """ adds given value to the end of this block """
        self.insert(len(self), value)

    def insert(self, index, value):
        """ inserts the given value into this block at the specified index """
        if self.containsOnlyPass:
            self.blocks.pop()
        if isinstance(value, (basestring, )):
            value = expression(left=value, right='', format='$left')
        self.blocks.insert(index, value)

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

    def dumpConfigValues(self, output, name):
        """ writes a sequence of lines given a config attribute name

        Lines may be callable.  Refer to the config.default module for
        details.
        """
        for lines in self.config.all(name, []):
            for line in lines:
                line = line(self) if callable(line) else line
                output.write('%s\n' % (line, ))

    def offset(self, indent):
        """ calculated indentation string

        @param indent integer indentation level
        @return string of spaces
        """
        return self.config.last('leadingIndent', '    ') * indent

    def formatExpression(self, value, rename=False):
        if isinstance(value, (dict, )):
            inner = value.copy()
            for key in (k for k in ('right', 'left', 'center', 'id') if k in value):
                inner[key] = self.formatExpression(value[key])
                #debug('%s', inner)
                if isinstance(inner[key], (basestring, )):
                    if inner[key] in self.classVariables and maybeAttr(self, 'isMethod'):
                        inner['format'] = 'self.%s' % inner['format']
                    if inner.get('rename'):
                        inner[key] = self.altId(inner[key])
            value = Template(inner['format']).substitute(inner)
        return value

    def addComment(self, value, index=0, prefix='#'):
        prefix = self.config.last('commentPrefix', prefix)
        ## don't use self.insert so that empty blocks don't have
        ## their pass statement popped
        self.blocks.insert(index, expression(left=prefix, right=value, format='$left$right'))

    def altId(self, value):
        """ Returns replacement value for given identifier. """
	alt = self.config.combined('identRenames')
        new = alt.get(value, value)
        return new
        top = self.top
        outer = top.outerMethod
        if outer or (new in top.instanceMembers):
            methargs = [v[1] for v in outer.parameters]
            if new in top.instanceMembers: # and methargs:
                if methargs[0] in ('cls', 'self'):
                    fmt = methargs[0] + '.%s'
                else:
                    fmt = '%s'
                new = fmt % new
        return new

    def altType(self, name):
        """ Returns replacement name for given type """
        alt = self.config.combined('typeRenames')
        return alt.get(name, name)

    def setConfigs(self, configs):
        """ sets the config on the root class so all instances share it """
        Block.config = Config(configs)

    def setIdent(self, ident):
        """ sets the name of this block """
        self.name = ident

    def addModifiers(self, modifiers):
        self.modifiers.extend(modifiers)

    def addClassVariables(self, decls, typ, modifiers):
        for decl in decls:
            self.variables.append(dict(ident=findIdent(decl), local=False))
            self.append(decl)

    def addLocalVariables(self, decls, typ, modifiers):
        for decl in decls:
            self.variables.append(dict(ident=findIdent(decl), local=True))
            self.append(decl)

    @property
    def commentHandlers(self):
        """ Returns the comment handlers from the config.

        """
        return self.config.handlers('commentHandlers')

    @property
    def containsOnlyPass(self):
        return self.blocks == passLine

    @property
    def classVariables(self):
        if maybeAttr(self, 'isMethod'):
            self = self.parent
        for item in self.variables:
            if not item.get('local'):
                yield item['ident']

    @property
    def localVariables(self):
        if maybeAttr(self, 'isMethod'):
            self = self.parent
        for item in self.variables:
            if item.get('local'):
                yield item['ident']




def findIdent(d):
    if isinstance(d, (basestring, )):
        return
    elif isinstance(d, (dict, )):
        if 'ident' in d:
            return d['ident']
        else:
            for key in d:
                v = findIdent(d[key])
                if v is not None:
                    return v
