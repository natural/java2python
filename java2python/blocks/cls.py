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
        for handler in self.config.handlers('classHandlers'):
            handler(self)
        offset = self.offset(indent)
        decl = self.decl()
        if decl:
            output.write('%s%s\n' % (offset, decl))
        Block.dump(self, output, indent+1)
        output.write('\n')

    def decl(self):
        """ generates a class statement accounting for base types

        """
        bases, name = self.bases, self.name
        if bases:
            bases = [self.formatExpression(b) for b in bases]
            decl = 'class %s(%s):' % (name, str.join(', ', bases))
        else:
            decl = 'class %s:' % (name, )
        return decl

    def addBases(self, bases):
	""" Extend this classes bases with the given sequence.

	"""
        self.bases.extend(bases)

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
