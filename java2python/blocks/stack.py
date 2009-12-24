#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" java2python.blocks.stack -> a simple stack of source blocks.

"""
from logging import info, debug, warn

from java2python import expression, isDict, maybeAttr, nameCounter, variable
from java2python.blocks import (AnnotationClass, AssertStatement,
				BreakStatement, Class, EnumerationClass,
				ExceptStatement, Method, Statement,
				SwitchStatement, )


class BlockStack(object):
    """ Simple stack of source blocks.

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
    def bottom(self):
        """ Returns item at the bottom of the stack. The stack is unchanged.

        """
        return self.stack[0]

    def maybePop(self, pop=True):
        """ some tree grammar callbacks only need to pop an item from the stack

        """
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
        return self.maybePop(pop=pop)

    def beginInterfaceDeclaration(self):
        parent = self.top
        cls = Class(parent=parent, name=None)
        parent.append(self.push(cls))
        return cls

    def endInterfaceDeclaration(self, pop=True):
        cls = self.top
        if maybeAttr(cls.parent, 'isClass'):
            cls.parent.variables.append(variable(ident=cls.name, cls=True))
        return self.maybePop(pop=pop)

    def beginAnnotationDeclaration(self):
        parent = self.top
        anno = AnnotationClass(parent=parent, name=None)
        parent.append(self.push(anno))
        return anno

    def endAnnotationDeclration(self, pop=True):
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
        return self.maybePop(pop=pop)

    def beginForEach(self):
        parent = self.top
        forblock = Statement(parent=parent, name='for')
        parent.append(self.push(forblock))
        return forblock

    def endForEach(self, pop=True):
        return self.maybePop(pop=pop)

    def beginForLoop(self, init, cond, update):
	parent = self.top
	whileloop = Statement(parent=parent, name='while', expr=cond)
	whileloop.updates = update
	parent.append(self.push(whileloop))
	return whileloop

    def endForLoop(self, pop=True):
	loop = self.maybePop(pop=pop)
	loop.extend(loop.updates)
        return loop

    def beginWhile(self, expr):
        parent = self.top
        whileblock = Statement(parent=parent, name='while', expr=expr)
        parent.append(self.push(whileblock))
        return whileblock

    def endWhile(self, pop=True):
        return self.maybePop(pop=pop)

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
        return self.maybePop(pop=pop)


    def beginIf(self, expr):
        parent = self.top
        ifstat = Statement(parent=parent, name='if', expr=expr)
        parent.append(self.push(ifstat))
        elsestat = Statement(parent=parent, name='else')
        return ifstat, elsestat

    def endIf(self, pop=True):
        return self.maybePop(pop=pop)

    def beginElse(self, stat):
        self.top.append(self.push(stat))

    def endElse(self, pop=True):
        return self.maybePop(pop=pop)

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
        return self.maybePop(pop=pop)

    def beginCatch(self, expr):
        parent = self.top
        exceptstat = ExceptStatement(parent=parent, name='except', expr=expr)
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
        breakstat = BreakStatement(parent=parent, name='break', expr=label)
        parent.append(breakstat)
        return breakstat

    def addContinue(self, label=None):
        parent = self.top
        if label is not None:
            label = self.makeComment(label)
        continuestat = ContinueStatement(parent=parent, name='continue', expr=label)
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
        cls = EnumerationClass(parent=parent, name=None)
        parent.append(self.push(cls))
        return cls

    def endEnumerationDeclaration(self, pop=True):
	""" Called by the tree grammar to finish processing an Enum.

	"""
        self.top.endDecl()
        return self.maybePop(pop=pop)

    def beginSwitch(self):
	""" Called by the tree grammar to begin processing a switch statement.

	"""
        parent = self.top
        ifstat = SwitchStatement(parent=parent, name='switch')
        parent.append(self.push(ifstat))
        return ifstat

    def addSwitchCase(self, expr):
	""" Called by the tree grammar to process a switch case.

	"""
        switch = self.top
        if switch.name == 'switch':
            switch.name = 'if'
            switch.expr = expression(switch.expr, expr, '$left == $right')
            self.push(switch)
        else:
            elifstat = Statement(parent=switch.parent, name='elif')
	    expr = expression(switch.switchExpression, expr, '$left == $right')
            elifstat.setExpression(expr)
            switch.parent.append(self.push(elifstat))

    def addSwitchCaseDefault(self):
	""" Called by the tree grammar to process the default switch case.

	"""
        switch = self.top
        if switch.name == 'switch':
            pass
        else:
            elsestat = Statement(parent=switch.parent, name='else')
	    switch.elseExpression = elsestat
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
        withstat = Statement(parent=parent, name='with')
        parent.append(self.push(withstat))
        return withstat

    def endSync(self, pop=True):
	""" Called by the tree grammar to finish a synchronized statement.

	"""
	return self.maybePop(pop=pop)
