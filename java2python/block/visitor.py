#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import izip
from java2python.parser import tokens


class BaseVisitor(object):
    """ BaseVisitor -> Base class for AST visitors.

    """
    def walk(self, tree):
	""" Depth-first visiting of the given AST. """
	visitor = self.accept(tree)
	if visitor:
	    map(visitor.walk, tree.children)

    def accept(self, node):
	""" Accept a node, possibly creating a child visitor. """
	title = tokens.title(tokens.map.get(node.token.type))
	return getattr(self, 'accept{0}'.format(title), lambda n:self)(node)

    def acceptClass(self, node):
	""" Creates a new class.  Called on Module and Class templates. """
	name = node.firstChildOfType(tokens.IDENT).text
	self.variables.append(name)
	return self.factory.klass(name=name, parent=self)

    def walkThisWay(self, nodes, exprs):
	for node, expr in izip(nodes, exprs):
	    expr.walk(node)

