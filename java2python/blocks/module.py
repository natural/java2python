#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" java2python.blocks.module -> defines the Module block type.

"""
from java2python import expression
from java2python.blocks import Block


class Module(Block):
    """ Module -> block type for the representation of a Python module.

    """
    def __init__(self, infile, outfile):
        Block.__init__(self, name=self.getBaseName(infile, outfile))
        self.infile = infile
        self.outfile = outfile

    def dump(self, output, indent):
        """ Writes the string representation of this block

        """
        self.callWriters('modulePreambleWriters', output)
        for line in self.preamble:
            output.write('\n%s' % self.formatExpression(line))
        output.write('\n')
        Block.dump(self, output, indent)
        self.callWriters('moduleEpilogueWriters', output)

    def addPackage(self, value):
        """ Adds the given package name as a comment

        """
        self.addComment(value)

    def addImport(self, value, star):
	""" Adds the given import expression to the preamble

	"""
	if star:
	    expr = expression(right=value, format='from $right import *')
	else:
	    expr = expression(right=value, format='import $right')
	self.preamble.append(expr)

    @staticmethod
    def getBaseName(infile, outfile):
	""" Returns the base filename given an input and output name.

	"""
        basein = infile.split('.java')[0]
        baseout = outfile.split('.py')[0]
        return (baseout if baseout and baseout != '-' else basein)
