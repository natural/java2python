#!/usr/bin/env python
# -*- coding: utf-8 -*-
from java2python.sourcetypes.block import Block


class Variable(Block):
    """Variable is a defined class member variable or auto variable of the
    method.

    """
    def __init__(self, parent, name=None, expr=None):
        Block.__init__(self, parent=parent, name=name)
        self.expr = expr

    def setExpression(self, expr):
        """ sets the value of the expression for this Variable

        @param value expression (see formatExpression in Block class).
        @return None
        """
        self.expr = expr

    @property
    def isVariable(self):
        """ True if this instance is static

        @return if the variable is static return True
        """
        return True
