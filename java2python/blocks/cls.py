#!/usr/bin/env python
# -*- coding: utf-8 -*-
from logging import warn
from java2python import maybeAttr, expression, formatParameter
from java2python.blocks.block import Block


class Class(Block):
    defaultBases = []
    isClass = True

    def __init__(self, parent, name):
        Block.__init__(self, parent, name)
        self.bases = self.defaultBases[:]
        self.append('pass')

    def dump(self, output, indent):
        """ writes the string representation of this block

        @param output any writable file-like object
        @param indent indentation level of this block
        """
        for handler in self.config.handlers('classHandlers'):
            handler(self)
        offset = self.offset(indent)
        decl = self.decl()
        if decl:
            output.write('%s%s\n' % (offset, decl))
        Block.dump(self, output, indent+1)
        output.write('\n')


    def decl(self):
        """ generates a class statement accounting for base types

        @return class declaration as string
        """
        bases, name = self.bases, self.name
        if bases:
            bases = [self.formatExpression(b) for b in bases]
            decl = 'class %s(%s):' % (name, str.join(', ', bases))
        else:
            decl = 'class %s:' % (name, )
        return decl

    @property
    def initMethod(self):
        """ returns the __init__ method from this block """
        for meth in self.methods:
            if meth.name == '__init__':
                return meth

    @property
    def methods(self):
        """ returns all of the methods in this block

        """
        for block in self:
            if maybeAttr(block, 'isMethod'):
                yield block

    def addBases(self, bases):
        self.bases.extend(bases)



class AnnotationClass(Class):
    defaultBases = ['Annotation']


class EnumerationClass(Class):
    defaultBases = ['Enum']

    def __init__(self, parent, name):
        Class.__init__(self, parent, name)
        self.values = []

    def addEnumValue(self, ident, arguments):
        self.values.append((ident, arguments))

    def endDecl(self):
        values = self.values
        if all(args==None for ident, args in values):
            ## simple enum
            for ident, args in values:
                self.append(expression(ident, "'%s'" % ident, "$left = $right"))
        else:
            ## constructor-based enum
            append = self.parent.append
            cls = self.name
            fs = '$left.$center = $left($right)'
            for ident, args in values:
                ex = expression(cls, args, fs, center=ident, rename=True)
                append(ex)

