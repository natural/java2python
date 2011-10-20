#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" java2python.lang.selector -> """
from java2python.lang import tokens


class Selector(object):
    """ Selector -> base for selectors; provides operator methods. """

    def __add__(self, other):
        """ C + C => S

        Produces a Sibling selector from this one and the right hand
        side of the expression.
        """
	return Sibling(self, other)

    def __and__(self, other):
        """ C & C => S

        Produces a Descendant selector from this one and the right
        hand side of the expression.
        """
	return Descendant(self, other)

    def __call__(self, *args, **kwds):
        """ Subclasses must implement. """
        raise NotImplementedError('Selector class cannot be called.')

    def __getitem__(self, key):
        """ C[n] => S

        Produces an Nth child selector from this one at the given key.

        This is where we could support attribute selectors like C[type='void'].
        """
	return Nth(self, key)

    def __gt__(self, other):
        """ C > C => S

        Produces a Child selector from this one and the right hand
        side of the expression.
        """
	return Child(self, other)

    def walk(self, tree):
        """ Select items from the tree and from the tree children. """
        for item in self(tree):
            yield item
        for child in tree.children:
            for item in self.walk(child):
                yield item


class Token(Selector):
    """ Token(...) -> select tokens by matching attributes.

    """
    # channel=None, index=None, input=None, line=None, start=None, stop=None, text=None, type=None

    def __init__(self, **attrs):
        self.attrs = attrs
        if isinstance(attrs.get('type'), (basestring, )):
            self.attrs['type'] = getattr(tokens, attrs.get('type'))

    def __call__(self, tree):
        items = self.attrs.items()
        token = tree.token

        def match_or_call(k, v):
            if callable(v):
                return v(token)
            return getattr(token, k)==v

        if all(match_or_call(k, v) for k, v in items if v is not None):
            yield tree

    def __str__(self):
        items = self.attrs.items()
        keys = ('{}={}'.format(k, v) for k, v in items if v is not None)
	return 'Token({})'.format(', '.join(keys))


class Nth(Selector):
    """ E[n] ->  match any slice n of E

    Similar to the :nth-child pseudo selector in CSS, but without the
    support for keywords like 'odd', 'even', etc.
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

    Similar to the type selector in CSS.
    """
    def __init__(self, key, value=None):
	self.key = key if isinstance(key, int) else getattr(tokens, key)
	self.value = value

    def __call__(self, tree):
	if tree.token.type == self.key:
	    if self.value is None or self.value == tree.token.text:
		yield tree

    def __str__(self):
        val = '' if self.value is None else '={0}'.format(self.value)
	return 'Type({0}{1}:{2})'.format(tokens.map[self.key], val, self.key)


class Star(Selector):
    """ *    select any

    Similar to the * selector in CSS.
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
