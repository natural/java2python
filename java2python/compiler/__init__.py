#!/usr/bin/env python
# -*- coding: utf-8 -*-

from java2python.compiler.block import Module
from java2python.lang import (
    Lexer, Parser, LocalSourceStream, LocalTokenStream, LocalTreeAdaptor,
    walkTreeSelector,
    )


def buildAST(source, config=None, debug=False):
    sourceStream = LocalSourceStream(source)
    sourceLexer = Lexer(sourceStream)
    tokenStream = LocalTokenStream(sourceLexer)
    sourceParser = Parser(tokenStream, state=None)

    def callback(node):
	node.parser = sourceParser
	node.lexer = sourceLexer

    treeAdaptor = LocalTreeAdaptor(callback)
    sourceParser.setTreeAdaptor(treeAdaptor)
    returnScope = sourceParser.javaSource()

    if debug:
	for idx, tok in enumerate(sourceParser.input.tokens):
	    print '{0}  {1}'.format(idx, tok)
	print

    return returnScope.tree


def transformAST(tree, config):
    for selector, call in config.handlers('transforms'):
	for node in walkTreeSelector(tree, selector):
	    call(node)


if __name__ == '__main__':
    import sys
    tree = buildAST(open(sys.argv[1]).read(), debug=True)
    tree.dump(sys.stdout)
