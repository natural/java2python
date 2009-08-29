#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" java2python.blocks.stack -> a simple stack of source blocks.

"""
from logging import info, debug, warn
from java2python import *
from java2python.blocks import *


class BlockStack:
    """

    """
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

    def beginClassDeclaration(self):
        parent = self.top
        cls = Class(parent=parent, name=None)
        parent.append(self.push(cls))
        return cls

    def endClassDeclaration(self, pop=True):
        cls = self.top
        if maybeAttr(cls.parent, 'isClass'):
            cls.parent.variables.append(variable(ident=cls.name, cls=True))
        return self.maybePop(pop)

    def beginInterfaceDeclaration(self):
        parent = self.top
        cls = Class(parent=parent, name=None)
        parent.append(self.push(cls))
        return cls

    def endInterfaceDeclaration(self, pop=True):
        cls = self.top
        if maybeAttr(cls.parent, 'isClass'):
            cls.parent.variables.append(variable(ident=cls.name, cls=True))
        return self.maybePop(pop)

    def beginClassScopeDecls(self):
        pass

    def endClassScopeDecls(self):
        pass

    def beginMethodDecl(self):
        parent = self.top
        meth = Method(parent=parent, name=None)
        parent.append(self.push(meth))
        return meth

    def endMethodDecl(self, pop=True):
        meth = self.top
        cls = meth.parent
        if meth.name == '__init__':
            meth.maybeAddSuperCall()
        return self.maybePop(pop)

    def beginFor(self):
        parent = self.top
        forblock = Statement(parent=parent, name='for')
        parent.append(self.push(forblock))
        return forblock

    def endFor(self):
        return self.pop()

    def beginWhile(self, expr):
        parent = self.top
        whileblock = Statement(parent=parent, name='while', expr=expr)
        parent.append(self.push(whileblock))
        return whileblock

    def endWhile(self, pop=True):
        return self.maybePop(pop)

    def beginDo(self):
        parent = self.top
        doblock = Statement(parent=parent, name='while', expr='True')
        parent.append(self.push(doblock))
        return doblock

    def endDo(self, expr, pop=True):
        doblock = self.top
        expr = expression(expr, format="not $left")
        ifbreak = Statement(parent=doblock, name='if', expr=expr)
        ifbreak.append('break')
        doblock.append(ifbreak)
        return self.maybePop(pop)


    def beginIf(self, expr):
        parent = self.top
        ifstat = Statement(parent=parent, name='if', expr=expr)
        parent.append(self.push(ifstat))
        elsestat = Statement(parent=parent, name='else')
        return ifstat, elsestat

    def endIf(self, pop=True):
        return self.maybePop(pop)

    def beginElse(self, stat):
        self.top.append(self.push(stat))

    def endElse(self, pop=True):
        return self.maybePop(pop)

    def makeAssert(self, expr):
        parent = self.top
        assertstat = AssertStatement(parent=parent, name='assert', expr=expr)
        parent.append(assertstat)
        return assertstat

    def extendAssert(self, stat, expr):
        stat.setExpression(expression(stat.getExpression(), expr, "$left, $right"))

    def beginTry(self):
        parent = self.top
        trystat = Statement(parent=parent, name='try')
        parent.append(self.push(trystat))
        return trystat

    def endTry(self, pop=True):
        return self.maybePop(pop)

    def beginCatch(self, expr):
        parent = self.top
        exceptstat = ExceptStatement(parent=parent, name='except', expr=expr)
        parent.append(self.push(exceptstat))
        return exceptstat

    def endCatch(self, pop=True):
        return self.maybePop(pop)

    def beginTryFinally(self):
        pass

    def endTryFinally(self):
        pass


    def makeArrayCreator(self, new, count, types=()):
        """ Returns an expression value to use as an array constructor.

        The optional types sequence is ignored for now.

        NB:  It's probably not this easy.
        """
        debug('%s %s %s right=%s', new, count, types, count.get('right'))

        if count.get('format', None) == '${right}':
            fmt = '[$left() for __%s in range($right)]' % nameCounter()
        else:
            fmt = '[$right]'
        expr = expression(self.renameType(new), count, fmt)
        #warn('%s', expr)
        return expr
