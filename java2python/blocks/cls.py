#!/usr/bin/env python
# -*- coding: utf-8 -*-
from logging import warn
from java2python import maybeAttr
from java2python.blocks.block import Block


class Class(Block):
    isClass = True

    def __init__(self, parent, name):
        Block.__init__(self, parent, name)
        self.bases = []
        self.append('pass')

    def dump(self, output, indent):
        """ writes the string representation of this block

        @param output any writable file-like object
        @param indent indentation level of this block
        """
        for handler in self.handlers:
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
    def handlers(self):
        return self.config.handlers('classHandlers')

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

    @property
    def classVariables(self):
        return self.variables
