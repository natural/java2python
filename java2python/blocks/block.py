#!/usr/bin/env python
# -*- coding: utf-8 -*-
from cStringIO import StringIO
from logging import debug, info, warn
from re import sub as rxsub
from string import Template

from java2python import expression, maybeAttr, variable, findKey, isDict, passExpr
from java2python.config import Config


class Block(object):
    """ Base class for blocks of Python source code.

    """
    config = None
    passLine = [passExpr(), ]

    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.blocks = []
        self.decorators = []
        self.modifiers = []
        self.preamble = []
        self.epilogue = []
        self.variables = []

    def __iter__(self):
        """ to iterate over a block is to iterate over its blocks

        """
        for item in self.blocks:
            yield item

    def __len__(self):
        """ returns the length of this block

        """
        return len(self.blocks)

    def extend(self, sequence):
	""" adds values from sequence to end of this block

	"""
	for item in sequence:
	    self.append(item)

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

    @property
    def commentHandlers(self):
        """ Returns the comment handlers from the config.

        """
        return self.config.handlers('commentHandlers')

    @property
    def containsOnlyPass(self):
        """ Returns True if this block contains only a pass expression.

        """
        return self.blocks == self.passLine

    @property
    def isStatic(self):
        """ Returns True if this block is static, i.e., a static method

        """
        return 'static' in [self.formatExpression(m) for m in self.modifiers]

    @property
    def isPublic(self):
        """ Returns True if this block is public

        """
        return 'public' in [self.formatExpression(m) for m in self.modifiers]

    @property
    def isVoid(self):
        """ Returns True if this block is void

        """
        return self.type in ('void', None)

    @property
    def parents(self):
        """ yields each ancestor of this instance

        """
        p = self.parent
        while p:
            yield p
            p = p.parent

    @property
    def ___root(self):
        while self:
            if not self.parent:
                break
            self = self.parent
        return self

    def asString(self):
        """ Returns the python source code representation of this block

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
        if isDict(value):
            inner = value.copy()
            for key in (k for k in ('right', 'left', 'center', 'ident') if k in value):
                inner[key] = self.formatExpression(value[key])
                if isinstance(inner[key], (basestring, )):
                    if inner.get('rename'):
                        debug('%s %s rename: %s', self.__class__.__name__,
			      self.name, inner[key])
                        inner[key] = self.renameIdent(inner[key])
            value = Template(inner['format']).substitute(inner)
        return value

    def addComment(self, value, index=0, prefix='#'):
        """ adds a comment to this block

        this methods doesn't use self.insert so that empty blocks
        don't have their pass statement popped
        """
        self.insert(index, self.makeComment(value, prefix))

    def makeComment(self, value, prefix='#'):
        prefix = self.config.last('commentPrefix', prefix)
        return expression(prefix, value, '$left$right')

    def getVariable(self, ident, default=None):
        while self:
            for v in self.variables:
                if v.get('ident') == ident:
                    return v
            self = self.parent
        return default

    def altIdent(self, value):
        var = self.getVariable(value, {})
        fmt = None
        params = getattr(self, 'parameterIdents', [])
        if var:
            if var.get('cls') and var.get('ident') not in params:
                fmt = 'self.%s' if not maybeAttr(self, 'isStatic') else 'cls.%s'
        value = self.renameIdent(value)
        if fmt:
            value = fmt % value
        return value

    def renameIdent(self, ident):
        """ Returns a simple replacement for the given identifier

        """
	alt = self.config.combined('identRenames')
        return alt.get(ident, ident)

    def renameType(self, name):
        """ Returns replacement name for the given type

        """
        alt = self.config.combined('typeRenames')
        return alt.get(name, name)

    def setConfigs(self, configs):
        """ sets the config on the root class so all instances share it

        """
        Block.config = Config(configs)

    def setIdent(self, ident):
        """ sets the name of this block

        """
        self.name = ident

    def addModifiers(self, modifiers):
        """ extends this blocks modifiers with the given sequence

        """
        types = [(m, m.get('annotation')) for m in modifiers]
        self.decorators.extend(mod for mod, anno in types if anno)
        self.modifiers.extend(mod for mod, anno in types if not anno)

    def addVariables(self, decls, typ, modifiers, local=False, cls=False):
        """ adds given variable declarations to this block

        """
	typeMap = self.config.combined('typeValueMap')
	addVar = self.variables.append
        for decl in decls:
            if typ.get('array'):
                decl['format'] = '$left = []'
            if not decl.get('right'):
                decl['format'] = '$left = $right'
                decl['right'] = typeMap.get(typ['left'], 'None')
            addVar(variable(findKey(decl, 'ident'), local=local, cls=cls))
            self.append(decl)
