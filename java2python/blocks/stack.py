#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" java2python.blocks.stack -> a simple stack of source blocks.

"""
from logging import info, debug, warn
from java2python.blocks import Class, Method


class BlockStack:
    def __init__(self, initial):
        self.stack = [initial]

    def pop(self):
        """ Removes item at the top of the stack and returns it.

        """
        value = self.stack.pop()
        debug('%s', (value.name if hasattr(value, 'name') else value))
	return value

    def push(self, value):
        """ Puts a new item at the top of the stack.

        @param value any object
        """
        debug('%s', (value.name if hasattr(value, 'name') else value))
	self.stack.append(value)
        return value

    @property
    def top(self):
        """ Returns item at the top of the stack.  The stack is unchanged.

        """
        return self.stack[-1]

    @property
    def bottom(self):
        """ Returns item at the bottom of the stack. The stack is unchanged.

        """
        return self.stack[0]

    def maybePop(self, pop=True):
        if pop:
            return self.pop()

    def setIdent(self, ident):
        self.top.name = ident

    def setModifiers(self, modifiers):
        self.top.setModifiers(modifiers)

    def setParameters(self, params):
        self.top.setParameters(params)

    def beginTypeDeclaration(self):
        info('')
        parent = self.top
        cls = Class(parent=parent, name=None)
        parent.append(self.push(cls))
        return cls

    endTypeDeclaration = maybePop

    def beginClassScopeDecls(self):
        pass

    def endClassScopeDecls(self):
        pass

    def beginVoidMethodDecl(self):
        info('')
        parent = self.top
        meth = Method(parent=parent, name=None)
        meth.type = 'void'
        parent.append(self.push(meth))
        return meth

    endVoidMethodDecl = maybePop

    def setExpression(self, value):
        self.top.append(value)

    def setVarDecls(self, decls, typ, modifiers):
        warn('%s %s %s', decls, typ, modifiers)

    def formatFloatLiteral(self, value):
        """ Turns a java float into a syntactically correct python float.

        This could be a regular function, but having it here makes it
        easily callable within the tree grammar.
        """
        if value.startswith('.'):
            value = '0' + value
        if value.endswith(('f', 'd')):
            value = value[:-1]
        elif value.endswith(('l', 'L')):
            value = value[:-1] + 'L'
        return value

    @property
    def commentHandlers(self):
        """ Returns the comment handlers from the config.

        """
        return self.top.config.handlers('commentHandlers')
