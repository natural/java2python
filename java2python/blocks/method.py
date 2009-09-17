#!/usr/bin/env python
# -*- coding: utf-8 -*-
from string import Template
from java2python import parameter, expression, maybeAttr, formatParameter
from java2python.blocks.block import Block


class Method(Block):
    """

    """
    isMethod = True

    def __init__(self, parent, name):
        Block.__init__(self, parent, name)
        self.parameters = []
        self.append('pass')
        self.type = None

    def dump(self, output, indent):
        """ writes the string representation of this block

        """
        offset = self.offset(indent)
        for handler in self.config.handlers('methodHandlers'):
            handler(self)
        for fmt, seq in (('\n%s%s', self.preamble), ('\n%s@%s', self.decorators)):
            if seq:
                for item in seq:
                    item = self.formatExpression(item)
                    output.write(fmt % (offset, item))
        output.write('\n%s%s\n' % (offset, self.decl()))
        Block.dump(self, output, indent+1)

    def decl(self):
        """ generates a class statement accounting for base types

        """
        parameters = self.parameterIdents
        return 'def %s(%s):' % (self.name, str.join(', ', parameters))

    @property
    def parameterIdents(self):
        return [formatParameter(p) for p in self.parameters]


    def setType(self, value):
        self.type = value

    def addModifiers(self, modifiers):
        Block.addModifiers(self, modifiers)
        if self.isStatic:
            self.decorators.append('classmethod')

    def addParameters(self, params):
        if self.isStatic:
            first = parameter(ident='cls', type='object')
        else:
            first = parameter(ident='self', type='object')
        self.parameters.extend([first] + params)

    def addSuperCall(self, expr):
        expr.update(format="super(${left}, self).__init__(${right})",
                    left=self.parent.name, super=True)
        self.insert(0, expr)

    def maybeAddSuperCall(self):
        supers = [block.get('super') for block in self if maybeAttr(block, 'get')]
        if not any(supers):
            self.addSuperCall(expression())
