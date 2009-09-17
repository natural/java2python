#!/usr/bin/env python
# -*- coding: utf-8 -*-
from logging import warn
from java2python import parameter
from java2python.blocks.block import Block


class Statement(Block):
    isStatement = True
    initialPass = True

    def __init__(self, parent, name, expr=None):
        Block.__init__(self, parent, name)
        if self.initialPass:
            self.append('pass')
        self.setExpression(expr)

    def dump(self, output, indent):
        """ writes the string representation of this block

        """
        if self.isBadLabel or self.isNoOp:
            return
        name = self.name
        blocks = self.blocks
        offset = self.offset(indent)
        output.write('%s%s' % (offset, name))
        if self.expr:
            expr = self.formatExpression(self.expr)
            output.write(' %s' % (expr, ))
        if self.needsBlockIndicator:
            output.write(':\n')
        Block.dump(self, output, indent+1)

    @property
    def isBadLabel(self):
        """ True if instance is a break or continue statement outside
        of a while or for loop.

        """
        if self.name in ('break', 'continue'):
            names = [p.name for p in self.parents]
            return 'while' not in names and 'for' not in names

    @property
    def isNoOp(self):
        """ True if this instance does nothing, e.g., else:pass.

        """
        empty = not self.blocks or self.containsOnlyPass
        return self.name in ('else', 'finally') and empty

    @property
    def needsBlockIndicator(self):
        """ True if instance needs a colon written after its expression

        """
        return self.name in ('class', 'def', 'elif', 'else', 'except',
                             'finally', 'for', 'if', 'try', 'while', 'with', )


    def getExpression(self):
        return self.expr

    def setExpression(self, value):
        """ sets the value of the expression for this Statement

        @param value expression (see formatExpression in BasicBlock class).
        @return None
        """
        self.expr = value


class AssertStatement(Statement):
    initialPass = False


class BreakStatement(Statement):
    initialPass = False


class ContinueStatement(Statement):
    initialPass = False


class ExceptStatement(Statement):
    def setExpression(self, expr):
        renames = self.config.combined('exceptionRenames')
        expr['type'] = renames.get(expr['type'], expr['type'])
        expr['format'] = '(${type}, ), ${ident}'
        Statement.setExpression(self, expr)


class SwitchStatement(Statement):
    initialPass = False
    switchExpression = None

    def __init__(self, parent, name, expr=None):
        Statement.__init__(self, parent, name, expr)
        self.switchExpression = expr

    def setExpression(self, expr):
        self.expr = self.switchExpression = expr
