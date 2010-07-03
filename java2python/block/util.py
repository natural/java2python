#!/usr/bin/env python
# -*- coding: utf-8 -*-
def nodeChildren(node, pred=lambda c:True):
    """ Returns all children of the node that meet the predicate. """
    return [child for child in node.children if pred(child)]


def nodeChildrenOfType(node, type):
    """ Returns all children of the node that are of the given type. """
    return nodeChildren(node, lambda c:c.type==type)


def nodeFirstChild(node, pred=lambda c:True, default=None):
    """ Returns the first child of the node that meets the predicate. """
    try:
	return [child for child in node.children if pred(child)][0]
    except (IndexError, ):
	return default


def nodeFindChildren(node, pred=lambda c:True):
    """ Depth-first search that yields nodes meeting the predicate. """
    for child in node.children:
	if pred(child):
	    yield child
	for sub in nodeFindChildren(child, pred):
	    yield sub


def nodeFindChildrenOfType(node, type):
    """ Depth-first search that yields nodes of the given type. """
    return nodeFindChildren(node, lambda c:c.type==type)


def nodeFirstChildOfType(node, type):
    """ Returns the first child of the node that is of the given type. """
    return nodeFirstChild(node, lambda c:c.type==type)


def nodeParentType(node):
    """ Returns the type of the parent node. """
    return node.parent.type


class FS(object):
    l = '{left}'
    r = '{right}'
    lc = l + ':'
    lr = l + r
    lsr = l + ' ' + r
    lsrc = lsr + ':'
