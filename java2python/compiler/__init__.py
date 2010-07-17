#!/usr/bin/env python
# -*- coding: utf-8 -*-

from java2python.compiler.block import Module
from java2python.compiler.transformer import Transformer
from java2python.lang import (
    Lexer, Parser, LocalSourceStream, LocalTokenStream, LocalTreeAdaptor
    )


def buildAST(source, config=None, debug=False):
    sourceStream = LocalSourceStream(source)
    sourceLexer = Lexer(sourceStream)
    tokenStream = LocalTokenStream(sourceLexer)
    sourceParser = Parser(tokenStream, state=None)

    def callback(node):
	node.parser = sourceParser
	node.lexer = sourceLexer
	sourceLexer.transform(node)

    treeAdaptor = LocalTreeAdaptor(callback)
    sourceParser.setTreeAdaptor(treeAdaptor)
    returnScope = sourceParser.javaSource()

    if debug:
	for idx, tok in enumerate(sourceParser.input.tokens):
	    print '{0}  {1}'.format(idx, tok)
	print

    return returnScope.tree


def transformAST(tree, config):
    return # bah
    transformer = Transformer(config)
    transformer(tree)


if __name__ == '__main__':
    import sys
    tree = buildAST(open(sys.argv[1]).read(), debug=True)
    tree.dump(sys.stdout)
