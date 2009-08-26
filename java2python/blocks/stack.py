#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" java2python.blocks.stack -> a simple stack of source blocks.

"""
from logging import info, debug, warn
from java2python.blocks import Class, Method, Statement


class BlockStack:
    def __init__(self, initial):
        self.stack = [initial]

    def __getattr__(self, name):
        return getattr(self.top, name)

    def pop(self):
        """ Removes item at the top of the stack and returns it. """
        value = self.stack.pop()
        debug('%s', (value.name if hasattr(value, 'name') else value))
	return value

    def push(self, value):
        """ Puts a new item at the top of the stack. """
        debug('%s', (value.name if hasattr(value, 'name') else value))
	self.stack.append(value)
        return value

    @property
    def top(self):
        """ Returns item at the top of the stack.  The stack is unchanged. """
        return self.stack[-1]

    @property
    def bottom(self):
        """ Returns item at the bottom of the stack. The stack is unchanged. """
        return self.stack[0]

    def maybePop(self, pop=True):
        """ some tree grammar callbacks only need to pop an item from the stack """
        return self.pop() if pop else None

    def beginTypeDeclaration(self):
        parent = self.top
        cls = Class(parent=parent, name=None)
        parent.append(self.push(cls))
        return cls

    endTypeDeclaration = maybePop

    def beginClassScopeDecls(self):
        pass

    def endClassScopeDecls(self):
        pass

    def beginMethodDecl(self):
        parent = self.top
        meth = Method(parent=parent, name=None)
        parent.append(self.push(meth))
        return meth

    endMethodDecl = maybePop


    def beginFor(self):
        parent = self.top
        forblock = Statement(parent=parent, name='for')
        parent.append(self.push(forblock))
        return forblock

    def endFor(self):
        return self.pop()
