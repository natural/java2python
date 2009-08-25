#!/usr/bin/env python
# -*- coding: utf-8 -*-
from logging import warn
from java2python import parameter
from java2python.blocks.block import Block


class Method(Block):
    isMethod = True

    def __init__(self, parent, name):
        Block.__init__(self, parent, name)
        self.decorators = []
        self.parameters = []
        self.append('pass')
        self.type = None

    def dump(self, output, indent):
        """ writes the string representation of this block

        @param output any writable file-like object
        @param indent indentation level of this block
        """
        for handler in self.handlers:
            handler(self)
        offset = self.offset(indent)
        decos = self.decorators
        mods = self.modifiers
        comment = self.config.last('commentPrefix', '#')
        if mods:
            output.write('%s%s%s\n' % (offset, comment, ', '.join(mods)))

        if decos:
            for deco in decos:
                output.write('%s@%s\n' % (offset, deco))
        output.write('%s%s\n' % (offset, self.decl()))
        Block.dump(self, output, indent+1)


    def decl(self):
        """ generates a class statement accounting for base types

        @return class declaration as string
        """
        parameters, name = self.parameters, self.name
        parameters = [self.formatExpression(p) for p in parameters]
        return 'def %s(%s):' % (name, str.join(', ', parameters))

    @property
    def handlers(self):
        return self.config.handlers('methodHandlers')

    @property
    def isStatic(self):
        return 'static' in self.modifiers

    @property
    def isPublic(self):
        return 'public' in self.modifiers

    @property
    def isVoid(self):
        return self.type in ('void', None)

    def setModifiers(self, modifiers):
        Block.setModifiers(self, modifiers)
        if self.isStatic:
            self.decorators.append('classmethod')

    def setParameters(self, params):
        first = parameter('cls') if self.isStatic else parameter('self')
        params.insert(0, first)
        self.parameters.extend(params)

