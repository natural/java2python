#!/usr/bin/env python
# -*- coding: utf-8 -*-
from java2python.lang import tokens


class Transformer(object):
    def __init__(self, configs=()):
	self.configs = configs


class Selector(object):
    """ Selector -> base for selectors; provides operator methods.

    """
    def __add__(self, other):
	return Sibling(self, other)

    def __and__(self, other):
	return Descendant(self, other)

    def __getitem__(self, key):
	return Nth(self, key)

    def __gt__(self, other):
	return Child(self, other)


class Nth(Selector):
    """ E[n]    match any slice n of E

    """
    def __init__(self, e, key):
	self.e, self.key = e, key

    def __call__(self, tree):
	for etree in self.e(tree):
	    try:
		matches = tree.children[self.key]
	    except (IndexError, ):
		return
	    if not isinstance(matches, (list, )):
		matches = [matches]
	    for child in matches:
		yield child

    def __str__(self):
	return 'Nth({0})[{1}]'.format(self.e, self.key)


class Child(Selector):
    """ E > F    select any F that is a child of E

    """
    def __init__(self, e, f):
	self.e, self.f = e, f

    def __call__(self, tree):
	for ftree in self.f(tree):
	    for etree in self.e(tree.parent):
		yield ftree

    def __str__(self):
	return 'Child({0} > {1})'.format(self.e, self.f)


class Type(Selector):
    """ Type(T)    select any token of type T

    """
    def __init__(self, key, value=None):
	self.key = key if isinstance(key, int) else getattr(tokens, key)
	self.value = value

    def __call__(self, tree):
	if tree.token.type == self.key:
	    if self.value is None or self.value == tree.token.text:
		yield tree

    def __str__(self):
	## TODO: add value
	return 'Type({0}:{1})'.format(tokens.map[self.key], self.key)


class Star(Selector):
    """ *    select any

    """
    def __call__(self, tree):
	yield tree

    def __str__(self):
	return 'Star(*)'


class Descendant(Selector):
    """ E & F    select any F that is a descendant of E

    """
    def __init__(self, e, f):
	self.e, self.f = e, f

    def __call__(self, tree):
	for ftree in self.f(tree):
	    root, ftree = ftree, ftree.parent
	    while ftree:
		for etree in self.e(ftree):
		    yield root
		ftree = ftree.parent

    def __str__(self):
	return 'Descendant({0} & {1})'.format(self.e, self.f)


class Sibling(Selector):
    """ E + F    select any F immediately preceded by a sibling E

    """
    def __init__(self, e, f):
	self.e, self.f = e, f

    def __call__(self, node):
	parent = node.parent
	if not parent:
	    return
	for ftree in self.f(node):
	    index = node.parent.children.index(ftree)
	    if not index:
		return
	    previous = node.parent.children[index-1]
	    for child in self.e(previous):
		yield ftree

    def __str__(self):
	return 'Sibling({0} + {1})'.format(self.e, self.f)


def walkSelector(tree, selector):
    for item in selector(tree):
	yield item
    for child in tree.children:
	for item in walkSelector(child, selector):
	    yield item


if __name__ == '__main__':
    import sys
    from java2python.config import Config
    from java2python.compiler import buildAST

    source = open(sys.argv[1]).read()
    tree = buildAST(source, Config(()))
    tree.dump(sys.stdout)


    selectors = [
	Type('EXPR'),
	Type('QUALIFIED_TYPE_IDENT') > Type('IDENT'),
        Type('CLASS')[2],
	Type('METHOD_CALL') & Type('IDENT'),
	Type('IDENT') + Type('IDENT'),
    ]

    for index, selector in enumerate(selectors):
	print '{0}: {1}\n   ==== {2}'.format(index, selector.__doc__.strip(), selector)
	for node in walkSelector(tree, selector):
	    name = str(node)
	    ntype = tokens.map[node.type]
	    args = (name, '') if name == ntype else (ntype, name)
	    print '{0}---- match: {1} {2}'.format(*(' '*8, )+args)
	print
