#!/usr/bin/env python
# -*- coding: utf-8 -*-
from logging import warn
from java2python import parameter, expression, maybeAttr
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

    def setType(self, value):
        self.type = value

    @property
    def handlers(self):
        return self.config.handlers('methodHandlers')



    def addModifiers(self, modifiers):
        Block.addModifiers(self, modifiers)
        if self.isStatic:
            self.decorators.append('classmethod')

    def addParameters(self, params):
        first = parameter('cls') if self.isStatic else parameter('self')
        first['type'] = 'object'
        params.insert(0, first)
        self.parameters.extend(params)


    def addSuperCall(self, expr):
        expr.update(format="super(${left}, self).__init__(${right})",
                    left=self.parent.name, super=True)
        self.insert(0, expr)

    def maybeAddSuperCall(self):
        supers = [block.get('super') for block in self if maybeAttr(block, 'get')]
        if not any(supers):
            self.addSuperCall(expression())

    @property
    def classVariables(self):
        return self.parent.classVariables
