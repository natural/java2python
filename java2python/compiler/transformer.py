#!/usr/bin/env python
# -*- coding: utf-8 -*-


# works:
# *                 match any token
# E                 match any token of type E
# E F               match any F token that is a descendant of an E token
# E > F             match any F token that is a child of an E token
# E, F              match any E token and any F token
# E + F             match any F token immediately preceded by a sibling token E
# E[n]              match any n-th child of E token

# E:first-child     match any E token when E is the first child of its parent
# E[fu]             match any E token with the 'fu' attribute set (any value)
# E[fu="bar"]       match any E token with the 'fu' attribute is exactly equal to 'bar'


##
# Configuration-based tree transformer.
from java2python.lang import tokens

from antlr3 import ANTLRStringStream, CommonTokenStream, Lexer, Parser
from antlr3.tree import CommonTreeAdaptor, CommonTree



def parseSelector(text):
    return

s1 = "METHOD_CALL DOT DOT (IDENT IDENT)"
s1 = [tokens.METHOD_CALL, tokens.DOT, tokens.DOT, []]
s1 = "" # [method, dot, dot, [ident, ident]]
selectors = (
    [tokens.METHOD_CALL, ],
    [tokens.METHOD_CALL, tokens.DOT, tokens.DOT, tokens.IDENT, ],
    )

class Transformer(object):
    def __init__(self, configs=()):
	self.configs = configs

    def __call__(self, tree):
	for selector in selectors:
	    if self.match(selector, tree):
		print '######### match:: ', selector

    def match(self, selector, tree):
	if not selector:
	    return True # false?
	first, more = selector[0], selector[1:]
	print '######', first, more
	if first == tree.type:
	    if more:
		return self.match(more, tree.children[0])
	    return True
	for node in tree.children:
	    if self.match(selector, node):
		return True
    def blah():
	for node in tree.children:
	    #title = 'transform{0}'.format(tokens.title(tokens.map[node.type]))
	    #method = getattr(self, title, None)
	    #if method:
		#method(node)
	    self(node)


    def __transformMethodCall(self, node):
	if node.children:
	    child = node.children[0]
	    if child.type == tokens.DOT:
		if child.children:
		    gchild = child.children[0]
		    if gchild.type == tokens.DOT:
			if len(gchild.children) == 2:
			    if gchild.children[0].type == tokens.IDENT and \
				   gchild.children[1].type == tokens.IDENT:
			        print '########## method call:', node, child.text,
				print gchild.text, gchild.children


def selectorDump(root, i=0):
    token = root.token
    typeName = selectorTokenNames[token.type]
    text = token.text
    if text != typeName:
	print '{0}{1}:{2}'.format('    '*i, typeName, text)
    else:
	print '{0}{1}'.format('    '*i, typeName)
    for child in root.children:
	selectorDump(child, i+1)


if __name__ == '__main__':
    import sys
    from java2python.config import Config
    from java2python.compiler import buildAST

    #source = open(sys.argv[1]).read()
    #tree = buildAST(source, Config(()))
    #tree.dump(sys.stdout)


    selectors = [
	'(*)',
	'(FU)',
	'(FU (BAR (BAZ)))',
	'(PARENT (CHILD))',
	'(APAR (ARRAY[1] (ARRAY[2])))',
#	'FIRST["r1"] SEC["r2"] THIRD["r3"] YY[4] * ZZ',
#	'FIRST["r1"] > SEC["r2"] THIRD["r3"]',
	]
    for index, selector in enumerate(selectors):
	print '{0}: "{1}"'.format(index, selector)
	for tree in  parseSelector(selector):
	    selectorDump(tree)
	    print
