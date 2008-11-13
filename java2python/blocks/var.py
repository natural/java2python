#!/usr/bin/env python
# -*- coding: utf-8 -*-
from java2python.blocks.base import BasicBlock


class Variable(BasicBlock):
    """Variable is a defined class member variable or auto variable of the
    method.

    """
    def __init__(self, parent, name=None, expr=None):
        BasicBlock.__init__(self, parent=parent, name=name)
        self.expr = expr
        self.isVariable = True

    def setExpression(self, expr):
        """ sets the value of the expression for this Variable

        @param value expression (see formatExpression in BasicBlock class).
        @return None
        """
        self.expr = expr

