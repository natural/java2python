#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" java2python.blocks.method -> defines the Method block type.

"""
from java2python import clsParam, selfParam, expression, maybeAttr, formatParameter
from java2python.blocks import Block


class Method(Block):
    """ Method -> block type for representing translated methods.

    """
    isMethod = True

    def __init__(self, parent=None, name=None):
        Block.__init__(self, parent, name)
        self.parameters = []
        self.append('pass')

    def dump(self, output, indent):
        """ Writes the string representation of this block

        """
        offset = self.offset(indent)
	self.callHandlers('methodHandlers')
        for fmt, seq in (('\n%s%s', self.preamble), ('\n%s@%s', self.decorators)):
            if seq:
                for item in seq:
                    item = self.formatExpression(item)
                    output.write(fmt % (offset, item))
        output.write('\n%s%s\n' % (offset, self.decl))
        Block.dump(self, output, indent+1)

    @property
    def decl(self):
        """ generates a class statement accounting for base types

        """
        parameters = self.parameterIdents
        return 'def %s(%s):' % (self.name, str.join(', ', parameters))

    @property
    def parameterIdents(self):
	""" Returns a list of formatted parameters for this method.

	"""
        return [formatParameter(p) for p in self.parameters]

    def addModifiers(self, modifiers):
	""" Adds modifiers to this method.  May also add classmethod decorator.

	"""
        Block.addModifiers(self, modifiers)
	if self.isStatic:
            self.decorators.append('classmethod')

    def addParameters(self, params):
	""" Adds parameters to this method.

	"""
	first = clsParam() if self.isStatic else selfParam()
        self.parameters.extend([first] + params)

    def addSuperCall(self, expr):
	""" Adds a super call to the given expression and inserts it
            as a child of this method.

	"""
        expr.update(format="super(${left}, self).__init__(${right})",
                    left=self.parent.name, super=True)
        self.insert(0, expr)

    def maybeAddSuperCall(self):
	""" Adds an empty super call if any child of this method has a
            super indicator.

	"""
        supers = [block.get('super') for block in self if maybeAttr(block, 'get')]
        if not any(supers):
            self.addSuperCall(expression())
