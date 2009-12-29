#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" java2python.blocks.cls -> defines the Class block type and various subtypes.

"""
from java2python import expression
from java2python.blocks import Class


class Enumeration(Class):
    """ Enumeration -> block type for representing translated enumerations.

    """
    defaultBases = ['Enum']

    def __init__(self, parent=None, name=None):
        Class.__init__(self, parent, name)
        self.values = []

    def addEnumValue(self, ident, arguments, annotations):
	""" Called by the tree parser to add an enumerated value.

	"""
        self.values.append((ident, arguments))

    def endDecl(self):
	""" Called by the block stack to finalize the enumeration.

	"""
        values = self.values
        if all(args==None for ident, args in values):
            ## simple enum
            for ident, args in values:
                self.append(expression(ident, "'%s'" % ident, "$left = $right"))
        else:
            ## constructor-based enum
            append = self.parent.append
            cls = self.name
            fs = '$left.$center = $left($right)'
            for ident, args in values:
                ex = expression(cls, args, fs, center=ident, rename=True)
                append(ex)

