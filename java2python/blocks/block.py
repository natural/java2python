#!/usr/bin/env python
# -*- coding: utf-8 -*-
from cStringIO import StringIO
from logging import debug, info, warn
from re import sub as rxsub
from string import Template

from java2python import expression, maybeAttr, variable
from java2python.config import Config


class Block:
    """ Base class for blocks of Python source code.

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
        """ to iterate over a block is to iterate over it's blocks

        """
        for item in self.blocks:
            yield item

    def __len__(self):
        """ returns the length of this block

        """
        return len(self.blocks)

    def append(self, value):
        """ adds given value to the end of this block

        """
        self.insert(len(self), value)

    def insert(self, index, value):
        """ inserts the given value into this block at the specified index

        """
        if self.containsOnlyPass:
            self.blocks.pop()
        if isinstance(value, (basestring, )):
            value = expression(left=value, format='$left')
        self.blocks.insert(index, value)

    passLine = [expression(left='pass', right='', format='$left')]

    @property
    def commentHandlers(self):
        """ Returns the comment handlers from the config.

        """
        return self.config.handlers('commentHandlers')

    @property
    def containsOnlyPass(self):
        return self.blocks == self.passLine

    @property
    def isStatic(self):
        return 'static' in self.modifiers

    @property
    def isPublic(self):
        return 'public' in self.modifiers

    @property
    def isVoid(self):
        return self.type in ('void', None)

    def asString(self):
        """ asString() -> python source code representation of this block

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
        debug('%s %s : %s', self.__class__.__name__, self.name, self.variables)
        offset = self.offset(indent)
        for item in self:
            if hasattr(item, 'dump'):
                item.dump(output, indent)
            else:
                item = self.formatExpression(item)
                if item.strip():
                    item = '%s%s\n' % (offset, item)
                else:
                    item = '\n'
                output.write(item)

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

        """
        return self.config.last('leadingIndent', '    ') * indent

    def formatExpression(self, value, rename=False):
        """ formats nested dictionaries, substituting as necessary

        """
        if isinstance(value, (dict, )):
            inner = value.copy()
            for key in (k for k in ('right', 'left', 'center', 'id') if k in value):
                inner[key] = self.formatExpression(value[key])
                if isinstance(inner[key], (basestring, )):
                    if inner.get('rename'):
                        debug('%s %s rename: %s', self.__class__.__name__, self.name, inner[key])
                        inner[key] = self.renameIdent(inner[key])
            value = Template(inner['format']).substitute(inner)
        return value

    def addComment(self, value, index=0, prefix='#'):
        """ adds a comment to this block

        this methods doesn't use self.insert so that empty blocks
        don't have their pass statement popped
        """
        prefix = self.config.last('commentPrefix', prefix)
        comment = expression(prefix, value, '$left$right')
        self.blocks.insert(index, comment)

    def getVariable(self, ident):
        while self:
            for v in self.variables:
                if v.get('ident') == ident:
                    return v
            self = self.parent
        return {}

    def altIdent(self, value):
        var = self.getVariable(value)
        fmt = None
        if var:
            if var.get('cls'):
                fmt = 'self.%s' if not maybeAttr(self, 'isStatic') else 'cls.%s'
        value = self.renameIdent(value)
        if fmt:
            value = fmt % value
        return value

    def renameIdent(self, value):
        """ Returns a simple replacement value for the given identifier

        """
	alt = self.config.combined('identRenames')
        return alt.get(value, value)

    def renameType(self, name):
        """ Returns replacement name for the given type

        """
        alt = self.config.combined('typeRenames')
        return alt.get(name, name)

    def oldAltIdFragment(self):
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

    def setConfigs(self, configs):
        """ sets the config on the root class so all instances share it

        """
        Block.config = Config(configs)

    def setIdent(self, ident):
        """ sets the name of this block

        """
        self.name = ident

    def addModifiers(self, modifiers):
        self.modifiers.extend(modifiers)

    def addClassVariables(self, decls, typ, modifiers):
        for decl in decls:
            self.variables.append(variable(self.findIdent(decl), cls=True))
            self.append(decl)

    def addLocalVariables(self, decls, typ, modifiers):
        for decl in decls:
            self.variables.append(variable(self.findIdent(decl), local=True))
            self.append(decl)

    def findIdent(self, mapping):
        if isinstance(mapping, (dict, )):
            if 'ident' in mapping:
                return mapping['ident']
            for key in mapping:
                v = self.findIdent(mapping[key])
                if v is not None:
                    return v
