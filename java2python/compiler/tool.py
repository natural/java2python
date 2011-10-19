#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" java2python.compiler.tool -> """
##
# This module can be run as a script, e.g.:
#
#    $ python -m java2python.compiler.tool ./SomeClass.java

from java2python.lang import Lexer, Parser, StringStream, TokenStream, TreeAdaptor


def buildAST(source, config=None):
    lexer = Lexer(StringStream(source))
    parser = Parser(TokenStream(lexer))
    adapter = TreeAdaptor(lexer, parser)
    parser.setTreeAdaptor(adapter)
    scope = parser.javaSource()
    return scope.tree


def transformAST(tree, config):
    for selector, call in config.last('astTransforms', ()):
        for node in selector.walk(tree):
	    call(node, config)


def buildJavaDocAST(source):
    from java2python.lang.JavaDocLexer import JavaDocLexer
    from java2python.lang.JavaDocParser import JavaDocParser
    lexer = JavaDocLexer(StringStream(source))
    parser = JavaDocParser(TokenStream(lexer))
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
