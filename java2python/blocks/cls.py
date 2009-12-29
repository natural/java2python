#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" java2python.blocks.cls -> defines the Class block type and various subtypes.

"""
from java2python import maybeAttr, expression, formatParameter
from java2python.blocks import Block


class Class(Block):
    """ Class -> block type for representing translated classes.

    """
    defaultBases = []
    isClass = True

    def __init__(self, parent=None, name=None, **kwds):
        Block.__init__(self, parent, name)
        self.bases = self.defaultBases[:]
        self.append('pass')
	for key, value in kwds.items():
	    setattr(self, key, value)

    def dump(self, output, indent):
        """ Writes the string representation of this block

        """
        offset = self.offset(indent)
	self.callHandlers('classHandlers')
	self.callHandlers('classAnnotationHandlers')
        for fmt, seq in (('\n%s%s\n', self.preamble), ('\n%s@%s\n', self.decorators)):
            if seq:
                for item in seq:
                    item = self.formatExpression(item)
                    output.write(fmt % (offset, item))
        output.write('%s%s\n' % (offset, self.decl))
        Block.dump(self, output, indent+1)
        output.write('\n')

    @property
    def decl(self):
        """ generates a class statement accounting for base types

        """
	bases, decl, args = self.bases, 'class %s:', (self.name, )
        if bases:
            bases = [self.formatExpression(b) for b in bases]
            decl, args = 'class %s(%s):', (self.name, str.join(', ', bases))
        return decl % args

    @property
    def initMethod(self):
        """ Returns the __init__ method from this block or None

	"""
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
	""" Extend this classes bases with the given sequence.

	"""
        self.bases.extend(bases)
