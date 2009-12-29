#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" java2python.blocks.stack -> a simple stack of source blocks.

"""
from functools import partial
from logging import info, debug, warn

from java2python import expression, isDict, maybeAttr, nameCounter, variable
from java2python.blocks import Class, Enumeration, Method, Statement


assertStatement = partial(Statement, name='assert')
breakStatement = partial(Statement, name='break')
continueStatement = partial(Statement, name='continue')
elifStatement = partial(Statement, name='elif')
elseStatement = partial(Statement, name='else')
exceptStatement = partial(Statement, name='except')
forStatement = partial(Statement, name='for')
ifStatement = partial(Statement, name='if')
tryStatement = partial(Statement, name='try')
whileStatement = partial(Statement, name='while')
withStatement = partial(Statement, name='with')


class BlockStack(object):
    """ BlockStack -> stack of block objects for the tree parser.

    """
    def __init__(self, initial):
        self.stack = [initial]

    def __getattr__(self, name):
	""" Defers missing attribute lookup to the top block.

	"""
        return getattr(self.top, name)

    def pop(self):
        """ Removes item at the top of the stack and returns it.

        """
        value = self.stack.pop()
        debug('%s', maybeAttr(value, 'name', default=value))
	return value

    def push(self, value):
        """ Puts a new item at the top of the stack.

        """
        debug('%s', maybeAttr(value, 'name', default=value))
	self.stack.append(value)
        return value

    @property
    def top(self):
        """ Returns item at the top of the stack.  The stack is unchanged.

        """
        return self.stack[-1]

    @property
    def previousOrTop(self):
	try:
	    return self.stack[-2]
	except (IndexError, ):
	    return self.top

    @property
    def bottom(self):
        """ Returns item at the bottom of the stack. The stack is unchanged.

        """
        return self.stack[0]

    def maybePop(self, pop=True):
        """ some tree grammar callbacks only need to pop an item from the stack

        """
        return self.pop() if pop else None

    def beginClassDeclaration(self):
	""" Called by the tree grammar to begin processing a class declaration

	"""
        parent = self.top
        cls = Class(parent=parent)
        parent.append(self.push(cls))
        return cls

    def endClassDeclaration(self, pop=True):
	""" Called by the tree grammar to finish processing a class declaration

	"""
        cls = self.top
        if maybeAttr(cls.parent, 'isClass'):
            cls.parent.variables.append(variable(ident=cls.name, cls=True))
        return self.maybePop(pop=pop)

    def beginInterfaceDeclaration(self):
	""" Called by the tree grammar to begin processing an interface

	"""
        parent = self.top
        cls = Class(parent=parent)
        parent.append(self.push(cls))
        return cls

    def endInterfaceDeclaration(self, pop=True):
	""" Called by the tree grammar to finish processing an interface

	"""
        cls = self.top
        if maybeAttr(cls.parent, 'isClass'):
            cls.parent.variables.append(variable(ident=cls.name, cls=True))
        return self.maybePop(pop=pop)

    def beginAnnotationDeclaration(self):
	""" Called by the tree grammar to begin processing an annotation

	"""
        parent = self.top
        anno = Class(parent=parent, isAnnotation=True)
        parent.append(self.push(anno))
        return anno

    def endAnnotationDeclration(self, pop=True):
	""" Called by the tree grammar to finish processing an annotation

	"""
        return self.maybePop(pop=pop)

    def addAnnotationMethod(self, modifiers, typ, ident, default=None):
        if not isDict(default):
            values = self.config.combined('typeValueMap')
            default = typ.copy()
            default['left'] = values.get(default['left'], default['left'])
        decl = expression(self.renameIdent(ident), default, "$left = $right")
        self.append(decl)

    def beginClassScopeDecls(self):
        pass

    def endClassScopeDecls(self):
        pass

    def beginMethodDecl(self, type=None, ident=None):
        parent = self.top
        meth = Method(parent=parent)
	if type is not None:
	    meth.setType(type)
	if ident is not None:
	    meth.setIdent(ident)
        parent.append(self.push(meth))
        return meth

    def endMethodDecl(self, pop=True):
        meth = self.top
        cls = meth.parent
        if meth.name == '__init__':
            meth.maybeAddSuperCall()
        return self.maybePop(pop=pop)

    def beginForEach(self):
        parent = self.top
        forblock = forStatement(parent=parent)
        parent.append(self.push(forblock))
        return forblock

    def endForEach(self, pop=True):
        return self.maybePop(pop=pop)

    def beginForLoop(self, init, cond, update):
	parent = self.top
	whileloop = whileStatement(parent=parent, expr=cond)
	whileloop.updates = update
	parent.append(self.push(whileloop))
	return whileloop

    def endForLoop(self, pop=True):
	loop = self.maybePop(pop=pop)
	loop.extend(loop.updates)
        return loop

    def beginWhile(self, expr):
        parent = self.top
        whileblock = whileStatement(parent=parent, expr=expr)
        parent.append(self.push(whileblock))
        return whileblock

    def endWhile(self, pop=True):
        return self.maybePop(pop=pop)

    def beginDo(self):
        parent = self.top
        doblock = whileStatement(parent=parent, expr='True')
        parent.append(self.push(doblock))
        return doblock

    def endDo(self, expr, pop=True):
        doblock = self.top
        expr = expression(expr, format="not $left")
        ifbreak = ifStatement(parent=doblock, expr=expr)
        ifbreak.append('break')
        doblock.append(ifbreak)
        return self.maybePop(pop=pop)


    def beginIf(self, expr):
        parent = self.top
        ifstat = ifStatement(parent=parent, expr=expr)
        parent.append(self.push(ifstat))
        elsestat = elseStatement(parent=parent)
        return ifstat, elsestat

    def endIf(self, pop=True):
        return self.maybePop(pop=pop)

    def beginElse(self, stat):
        self.top.append(self.push(stat))

    def endElse(self, pop=True):
        return self.maybePop(pop=pop)

    def makeAssert(self, expr):
        parent = self.top
        assertstat = assertStatement(parent=parent, expr=expr)
        parent.append(assertstat)
        return assertstat

    def extendAssert(self, stat, expr):
        stat.setExpression(expression(stat.getExpression(), expr, "$left, $right"))

    def beginTry(self):
        parent = self.top
        trystat = tryStatement(parent=parent)
        parent.append(self.push(trystat))
        return trystat

    def endTry(self, pop=True):
        return self.maybePop(pop=pop)

    def beginCatch(self, expr):
        parent = self.top
        exceptstat = exceptStatement(parent=parent, expr=expr)
        parent.append(self.push(exceptstat))
        return exceptstat

    def endCatch(self, pop=True):
        return self.maybePop(pop=pop)

    def beginTryFinally(self):
        pass

    def endTryFinally(self):
        pass

    def addBreak(self, label=None):
        parent = self.top
        if label is not None:
            label = self.makeComment(label)
        breakstat = breakStatement(parent=parent, expr=label)
        parent.append(breakstat)
        return breakstat

    def addContinue(self, label=None):
        parent = self.top
        if label is not None:
            label = self.makeComment(label)
        continuestat = continueStatement(parent=parent, expr=label)
        parent.append(continuestat)
        return continuestat

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
        return expr

    def addLabel(self, value):
        warn('Label unhandled: %s', value)
        if value:
            value = 'label:%s' % value
        self.addComment(value)

    def beginEnumerationDeclaration(self):
	""" Called by the tree grammar to begin processing an Enum.

	"""
        parent = self.top
        cls = Enumeration(parent=parent)
        parent.append(self.push(cls))
        return cls

    def endEnumerationDeclaration(self, pop=True):
	""" Called by the tree grammar to finish processing an Enum.

	"""
        self.top.endDecl()
        return self.maybePop(pop=pop)

    def beginSwitch(self, expr):
	""" Called by the tree grammar to begin processing a switch statement.

	"""
        parent = self.top
        switch = Statement(parent=parent, expr=expr, switchExpression=expr)
        parent.append(self.push(switch))
        return switch

    def addSwitchCase(self, expr):
	""" Called by the tree grammar to process a switch case.

	"""
        switch = self.top
	if switch.name is None:
            switch.name = 'if'
	    case = expression(switch.getExpression(), expr, '$left == $right')
            switch.setExpression(case)
            self.push(switch)
        else:
            elifstat = elifStatement(parent=switch.parent)
	    case = expression(switch.switchExpression, expr, '$left == $right')
            elifstat.setExpression(case)
            switch.parent.append(self.push(elifstat))

    def addSwitchCaseDefault(self):
	""" Called by the tree grammar to process the default switch case.

	"""
        switch = self.top
	if switch.name is not None:
            elsestat = elseStatement(parent=switch.parent)
            switch.parent.append(self.push(elsestat))

    def endSwitch(self, pop=True):
	""" Called by the tree grammar to finish processing a switch statement.

	"""
        return self.maybePop(pop=pop)

    def addThrow(self, expr):
	""" Called by the tree grammar to process a throw statement.

	"""
	raiseexpr = expression(right=expr, format='raise $right')
	self.top.append(raiseexpr)
	return raiseexpr

    def beginSync(self):
	""" Called by the tree grammar to begin a synchronized statement.

	"""
        parent = self.top
        withstat = withStatement(parent=parent)
        parent.append(self.push(withstat))
        return withstat

    def endSync(self, pop=True):
	""" Called by the tree grammar to finish a synchronized statement.

	"""
	return self.maybePop(pop=pop)
