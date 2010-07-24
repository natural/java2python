#!/usr/bin/env python
# -*- coding: utf-8 -*-

from java2python.compiler.block import Module
from java2python.lang import (
    Lexer, Parser,
    LocalSourceStream, LocalTokenStream, LocalTreeAdaptor,
    walkTreeSelector,
    )


def buildAST(source, config=None):
    lexer = Lexer(LocalSourceStream(source))
    parser = Parser(LocalTokenStream(lexer))

    def setNodeRecognizers(node):
	node.parser = parser
	node.lexer = lexer

    parser.setTreeAdaptor(LocalTreeAdaptor(setNodeRecognizers))
    scope = parser.javaSource()
    return scope.tree


def transformAST(tree, config):
    for selector, call in config.handlers('astTransforms'):
	for node in walkTreeSelector(tree, selector):
	    call(node, config)



def buildJavaDocAST(source):
    from java2python.lang.JavaDocLexer import JavaDocLexer
    from java2python.lang.JavaDocParser import JavaDocParser

    lexer = JavaDocLexer(LocalSourceStream(source))
    parser = JavaDocParser(LocalTokenStream(lexer))

    scope = parser.commentBody()
    return scope.tree


def walkJavaDoc(tree, callback=lambda x:None):
    pass


if __name__ == '__main__':
    import sys
    tree = buildAST(open(sys.argv[1]).read())
    for idx, tok in enumerate(tree.parser.input.tokens):
	print '{0}  {1}'.format(idx, tok)
    print
    tree.dump(sys.stdout)
