#!/usr/bin/env python
# -*- coding: utf-8 -*-
from java2python.blocks.block import Block


class Statement(Block):
    """ Statement -> specialized block type

    Unlike Block instances, Statement instances have expressions.  These
    expressions are evaluated before they're output.
    """
    def __init__(self, parent, name=None, expr=None):
        Block.__init__(self, parent=parent, name=name)
        self.expr = expr

    def dump(self, output, indent):
        """ writes the string representation of this block

        @param output any writable file-like object
        @param indent indentation level of this block
        @return None
        """
        name = self.name
        parents = self.allParents()
        lines = self.lines
        if self.isBadLabel or self.isNoOp:
            return
        offset = self.I(indent)
        output.write('%s%s' % (offset, name))
        if self.expr is not None:
            expr = self.formatExpression(self.expr)
            output.write(' %s' % (expr, ))
        if self.needsBlockIndicator:
            output.write(':')
        output.write('\n')
        if (not lines) and not name.startswith(('break', 'continue', 'raise', 'assert')):
            self.addSource('pass')
        Block.dump(self, output, indent+1)

    @property
    def isBadLabel(self):
        """ True if instance is a break or continue statement outside
        of a while or for loop.

        """
        if self.name in ('break', 'continue'):
            parent_names = [p.name for p in self.allParents()]
            if 'while' not in parent_names and 'for' not in parent_names:
                return True

    @property
    def isNoOp(self):
        """ True if this instance does nothing, e.g., else:pass.

        """
        return self.name in ('else', 'finally') and (not self.lines)

    @property
    def needsBlockIndicator(self):
        """ True if instance needs a colon written after its expression

        """
        return self.name in ('if', 'while', 'for', 'else', 'elif',
                             'try', 'except', 'finally')

    def setExpression(self, value):
        """ sets the value of the expression for this Statement

        @param value expression (see formatExpression in Block class).
        @return None
        """
        self.expr = value
