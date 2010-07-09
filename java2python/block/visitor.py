#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from functools import reduce
from itertools import izip

from java2python.parser import tokens


class Memo(object):
    def __init__(self):
	self.comments = set()


class BaseVisitor(object):
    """ BaseVisitor -> Base class for AST visitors.

    """
    commentSubs = [
	re.compile('^\s*/(\*)+'), re.compile('(\*)+/\s*$'), re.compile('^\s*//'),
    ]


    def accept(self, node, memo):
	""" Accept a node, possibly creating a child visitor. """
	title = tokens.title(tokens.map.get(node.token.type))
	call = getattr(self, 'accept{0}'.format(title), lambda n, m:self)
        return call(node, memo)

    def walk(self, tree, memo=None):
	""" Depth-first visiting of the given AST. """
	memo = Memo() if memo is None else memo

	self.handleComments(self, tree, tree.tokenStartIndex, memo.comments)
	visitor = self.accept(tree, memo)

	if visitor:
	    for child in tree.children:
		visitor.walk(child, memo)
	self.handleComments(visitor, tree, tree.tokenStopIndex, memo.comments)

    def zipWalk(self, nodes, visitors, memo):
	""" Walk the given nodes zipped with the given visitors. """
	for node, visitor in izip(nodes, visitors):
	    visitor.walk(node, memo)

    def handleComments(self, block, tree, index, cache):
	parser = tree.parser
	prefix = self.config.last('commentPrefix')
	csubs = self.commentSubs
	for comment in self.selectComments(parser, index, cache):
	    if comment.line == parser.input.tokens[index].line and getattr(block, 'isExpression'):
		## getting closer...
		block.tail += prefix + str(comment.text)
	    else:
		for line in [l for l in comment.text.split('\n') if l.strip()]:
		    line = reduce(lambda v, rx:re.sub(rx, '', v), csubs, line)
		    expr = self.factory.expr(left=prefix, right=line, parent=self)

    def selectComments(self, parser, stop, cache):
	pred = lambda k:k.type in tokens.commentTypes and k.index not in cache
	ctoks = [t for t in parser.input.tokens[0:stop] if pred(t)]
	cache.update(t.index for t in ctoks)
	return ctoks
