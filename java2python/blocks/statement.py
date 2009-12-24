#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" java2python.blocks.statement -> defines various Statement block types.

"""
from java2python.blocks.block import Block


class Statement(Block):
    """ Statement -> block type that represents a Python statement.

    """
    isStatement = True

    def __init__(self, parent=None, name=None, expr=None, **kwds):
        Block.__init__(self, parent, name)
	if self.needsInitialPass:
            self.append('pass')
        self.setExpression(expr)
	for key, value in kwds.items():
	    setattr(self, key, value)

    def dump(self, output, indent):
        """ Writes the string representation of this block

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
            return ('while' not in names) and ('for' not in names)

    @property
    def isNoOp(self):
        """ True if this instance does nothing, e.g., else:pass.

        """
        empty = not self.blocks or self.containsOnlyPass
        return (self.name in ('else', 'finally')) and empty

    @property
    def needsBlockIndicator(self):
        """ True if instance needs a colon written after its expression

        """
        return self.name in ('class', 'def', 'elif', 'else', 'except',
                             'finally', 'for', 'if', 'try', 'while', 'with', )

    @property
    def needsInitialPass(self):
	return self.name not in ('break', 'assert', 'continue', 'switch', )

    def getExpression(self):
	""" Gets the value of the expression for this Statement.

	"""
        return self.expr

    def setExpression(self, value):
        """ Sets the value of the expression for this Statement

        """
	if self.name == 'except':
	    renames = self.config.combined('exceptionRenames')
	    value.update(
		type=renames.get(value['type'], value['type']),
		format='(${type}, ), ${ident}',
	    )
        self.expr = value
