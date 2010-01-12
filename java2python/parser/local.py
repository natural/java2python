#!/usr/bin/env python
# -*- coding: utf-8 -*-
from antlr3 import Parser
from antlr3.tree import CommonTreeAdaptor
from java2python.blocks import BlockFactory
from java2python.config import Config


class LocalParser(Parser):
    """ Antlr parser subclass with block factory and comment handling.

    """
    def __init__(self, input, state=None):
	Parser.__init__(self, input, state=state)
	# makes instance usable when run as a script
	self.setRawComments([])
        self.setFactory(BlockFactory(Config([])))

    def setRawComments(self, value):
	""" Sets the comment sequence to the given value

	"""
        self.comments = value

    def setFactory(self, value):
	""" Sets the block factory to the given value

	"""
        self.factory = value

    def checkComments(self, node):
	"""  Called by the tree adapter below after each token is made

	"""
	start = node.token.start if hasattr(node, 'token') else node
	target = self.selectCommentsTarget()
	if target is None:
	    return
	for comment in self.popComments(start):
	    target.addComment(comment)

    def selectCommentsTarget(self):
	""" Feeble attempt to locate the most appropriate block for comments

	"""
	stacks = ('expr', 'method', 'klass', 'module')
	for name in stacks:
	    stack = getattr(self, 'py_%s_stack' % name)
	    if stack:
		return getattr(stack[-1], name)

    def popComments(self, start):
	""" Pops and returns comments before given starting point

	"""
	comments = []
	for item in self.comments:
	    if item[0] < start:
		comments.append(item)
	    else:
		break
	for comment in comments:
	    self.comments.remove(comment)
	return comments

    def checkCommentsLeading(self, token):
	""" Handles any leading comments.

	"""
	self.checkComments(token.start)

    def checkCommentsTrailing(self):
	""" Handles any trailing comments.

	"""
	if self.comments:
	    self.checkComments(self.comments[-1][1]+1)

    def fixFloatLiteral(self, value):
        """ Turns a java float into a syntactically correct python float.

        This could be a regular function, but having it here makes it
        easily callable within the grammar.
        """
        if value.startswith('.'):
            value = '0' + value
        if value.endswith(('f', 'd')):
            value = value[:-1]
        elif value.endswith(('l', 'L')):
            value = value[:-1] + 'L'
        return value


class LocalTreeAdaptor(CommonTreeAdaptor):
    """ Antlr tree subclass with hook for checking comments.

    """
    def __init__(self, callback):
	CommonTreeAdaptor.__init__(self)
	self.callback = callback

    def createWithPayload(self, payload):
	""" Invokes callback to check for comments as each node is created

	"""
        node = CommonTreeAdaptor.createWithPayload(self, payload)
	if node.token:
	    self.callback(node)
        return node
