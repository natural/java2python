#!/usr/bin/env python
# -*- coding: utf-8 -*-

from java2python.config import Config
from java2python.compiler import buildAST
from java2python.lang import tokens
from java2python.lang.selector import Token, Type


if __name__ == '__main__':
    import sys, os
    fn = os.path.join(os.path.dirname(__file__), 'Selector1.java')
    source = open(fn).read()
    tree = buildAST(source, Config(()))
    tree.dump(sys.stdout)

    selectors = [
#	Type('EXPR'),
#	Type('QUALIFIED_TYPE_IDENT') > Type('IDENT'),
#        Type('CLASS')[2],
#	Type('METHOD_CALL') & Type('IDENT'),
#	Type('IDENT') + Type('IDENT'),
        Type('CLASS') > Type('IDENT'),
        Type('IDENT', 'foo'),
        Token(text='foo'),
        Token(type='BLOCK_SCOPE', line=2) & Token(type='IDENT', text='foo')
    ]

    for index, selector in enumerate(selectors):
	print 'Selector Test {0}:\n   ==== {1}'.format(index, selector)
        for node in selector.walk(tree):
	    name = str(node)
	    ntype = tokens.map[node.type]
	    args = (name, '') if name == ntype else (ntype, name)
	    print '{0}---- match: {1} {2}'.format(*(' '*8, )+args)
            print '{0}---- token: {1}'.format(' '*8, node.dumps() )
	print
