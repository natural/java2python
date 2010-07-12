#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from functools import reduce
from itertools import ifilter, izip, tee

from java2python.parser import tokens


class Memo(object):
    """ Memo -> AST walking luggage.

    """
    def __init__(self):
	self.comments = set()
	self.index = 0


class BaseVisitor(object):
    """ BaseVisitor -> Base class for AST visitors.

    """
    commentSubs = (
	re.compile('^\s*/(\*)+'),
	re.compile('(\*)+/\s*$'),
	re.compile('^\s*//'),
    )

    def accept(self, node, memo):
	""" Accept a node, possibly creating a child visitor. """
	title = tokens.title(tokens.map.get(node.token.type))
	call = getattr(self, 'accept{0}'.format(title), lambda n, m:self)
        return call(node, memo)

    def walk(self, tree, memo=None):
	""" Depth-first visiting of the given AST. """
	if not tree:
	    return
	memo = Memo() if memo is None else memo
	self.insertComments(self, tree, tree.tokenStartIndex, memo)
	visitor = self.accept(tree, memo)
	if visitor:
	    for child in tree.children:
		visitor.walk(child, memo)
	self.insertComments(visitor, tree, tree.tokenStopIndex, memo)
	## does not pick up trailing comments

    def zipWalk(self, nodes, visitors, memo):
	""" Walk the given nodes zipped with the given visitors. """
	for node, visitor in izip(nodes, visitors):
	    visitor.walk(node, memo)

    def insertComments(self, block, tree, index, memo):
	""" Add comments to the block from tokens in the tree. """
	cache = memo.comments
	parser, prefix = tree.parser, self.config.last('commentPrefix', '# ')

	## the next for loop should read like this, but it's pretty
	## slow that way:
	#
	#pred = lambda k:k.type in tokens.commentTypes and k.index not in cache
	#for token in ifilter(pred, parser.input.tokens[0:index]):

	for token in parser.input.tokens[memo.index:index]:
	    if (token.type != 181 and token.type != 182) or token.index in cache:
		continue
	    cache.add(token.index)
	    isexp = getattr(block, 'isExpression', False)
	    if isexp and (token.line == parser.input.tokens[index].line):
  	        block.tail += '' if block.tail.startswith(prefix) else prefix
		block.tail += ''.join(self.stripComment(token.text))
	    else:
		for line in self.stripComment(token.text):
		    self.factory.comment(left=prefix, right=line, parent=self)
	memo.index = index

    def stripComment(self, text):
	""" Regex substitutions for comments; removes comment characters. """
	resub = lambda val, rx:re.sub(rx, '', val)
	for text in ifilter(unicode.strip, text.split('\n')):
	    yield reduce(resub, self.commentSubs, text)
