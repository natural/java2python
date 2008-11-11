#!/usr/bin/env python
from logging import debug
from java2python import maybeimport

## yes, one of those.
marker = object()


class SimplePythonSourceStack:
    """ A simple stack of source blocks.

    """
    def __init__(self, module):
	self.stack = [module]

    @property
    def top(self):
	return self.stack[-1]

    def makeArrayCreator(self, typ, ctor):
        ## it can't be this easy
        value = dict(left=typ, right=ctor, format='[$left() for _ in range($right)]')
        return value

    def makeMethodExpr(self, methexpr, methargs):
	debug('%s %s', methexpr, methargs)
        #methargs = [dict(format='$left', left=arg) for arg in methargs]
        methargs = methargs
        return dict(left=methexpr, right=methargs, format='$left($right)')

    def makeParamDecl(self, src, typ, isVariadic=False):
        exp = src.copy()
        exp['type'] = typ
        exp['format'] = '$left'
        if isVariadic:
            exp['id'] = '*' + exp['id']
        debug('(return value) %s %s %s', exp, typ, isVariadic)
        return exp

    def onAnnoMethod(self, name, annodecls, default):
	meth = self.onMethod(name)
	for annodecl in (annodecls or []):
            meth.addModifier(annodecl[0])
	if default:
	    src = 'return %s' % (default, )
	else:
	    src = 'pass'
        meth.addSource(src)
	self.pop()
	return meth

    def onAnnoType(self, name, modifiers):
	## lookup base class
	bases = ['object', ]
	klass = self.onClass(name, [], bases)
	return klass

    def onAssert(self, exp, arg=marker):
        debug('%s %s', exp, arg)
        if arg is not marker:
            src = dict(format='$left, $right', left=exp, right=arg)
        else:
            src = dict(format='$left', left=exp)
        stat = self.top.newStatement('assert')
        stat.setExpression(src)

    def onAssign(self, op, left, right):
        debug('%s %s %s', op, left, right)
        src = dict(format='$left %s $right' % op, left=left, right=right)
        self.top.addSource(src)

    def onBreak(self, label):
        debug('%s', label)
        ## ident doesn't need expression formatting, so we add the
        ## string directly.  same true below for the 'continue'
        ## statement.
        self.top.addSource('break' + (' #label:' + label if label else ''))

    def onClass(self, name, mods=None, extends=None, implements=None):
	debug('%s %s %s %s', name, mods, extends, implements)
	klass = self.top.newClass()
	klass.name = name

	def annoDecl(v):
	    s = []
	    for d in v:
		for k in d:
		    if len(k) == 2:
			s.append('%s=%s' % tuple(k))
		    else:
			s.append(k)
	    return ', '.join(s)

	for mod in (mods or []):
	    if isinstance(mod, basestring):
                klass.addModifier(mod)
	    elif isinstance(mod, list):
		name, inits = mod
		if inits:
		    suffix = '(' + annoDecl(inits) +  ')'
		else:
		    suffix = ''
		#name += suffix
                exp = dict(left=name, right=suffix, format='@$right($left)')
		klass.addModifier('@' + self.top.formatExpression(name))

	for base in (extends or []) + (implements or []):
	    klass.addBaseClass(base)
	self.push(klass)
	return klass

    def onContinue(self, label):
        debug('%s', label)
        self.top.addSource('continue' + (' # ' + label if label else ''))

    def onDo(self):
        debug('')
        stat = self.top.newStatement('while')
        stat.setExpression('True')
        self.push(stat)
        return stat

    def onDoFinish(self, stat, expr, pop=False):
        debug('%s %s %s', stat, expr, pop)
        ifstat = stat.newStatement('if')
        ifstat.newStatement('break')
        ifstat.setExpression(dict(format='not $left', left=expr))
        return (self.pop() if pop else None)

    def onEnum(self, name, mods=None, implements=None):
        debug('%s', name)
	klass = self.onClass(name)
	return klass

    def onEnumConstant(self, decl):
        name = decl['id']
        debug('%s', name)
        if name.startswith('<missing'):
            return
        for handler in self.top.config.last('enumConstantHandlers', ()):
            handler = maybeimport(handler)
            handler(self, decl)
        if 0: # not name.startswith('<missing'):
            ## use a simpler method
            from java2python.config.enumhandlers import pystrings, pyints
            pyints(self, decl)
        if 0:
            if 'klass' not in decl: # a new class for the enum constant was created
                #klass = self.onClass(name)
                #self.pop()
                pass
            else:
                if not name.startswith('<missing'):
                    ## use a simpler method
                    from java2python.config.enumhandlers import pystrings, pyints
                    pyints(self, decl)

    def onFor(self, expressions, condition):
        debug('%s %s', expressions, condition)
        blk, stat = self.top.newFor()
        #for expr in expressions:
        #    self.top.addSource(expr)
        if condition is None:
            condition = 'True'
        stat.setExpression(condition)
        stat.addSource('pass')
        self.push(stat)
        return blk, stat

    def onForEach(self, typ, ident, exp):
        debug('%s %s %s', typ, ident, exp)
        blk, stat = self.top.newForEach()
        src = dict(format='$left in $right', left=ident, right=exp)
        stat.setExpression(src)
        self.push(stat)
        return blk, stat

    def onForFinish(self, stat, updates, pop=False):
        for update in updates:
            stat.addSource(update)
        return (self.pop() if pop else None)

    def onImportDecl(self, decl, isStatic, isStar):
        isStatic, isStar = bool(isStatic), bool(isStar)
        debug('%s', decl)
        for handler in self.top.config.last('importHandlers', ()):
            handler = maybeimport(handler)
            handler(self, decl, isStatic, isStar)
        return decl

    def onMethod(self, name, mods=None, params=None, pop=False):
	debug('%s %s %s', name, mods, params)
	meth = self.top.newMethod()
	meth.name = name
	for mod in (mods or []):
	    meth.addModifier(mod)
	for param in (params or []):
	    #if len(param) == 2:
	    #    param += [None]
	    t, p, a = param.get('type', ''), param.get('left', ''), param.get('array')
	    meth.addParameter(t, p)
	self.push(meth)
        return (self.pop() if pop else meth)

    def onPackageDecl(self, decl):
        debug('%s', decl)
        for handler in self.top.config.last('packageHandlers', ()):
            handler = maybeimport(handler)
            handler(self, decl)
        return decl

    def onReturn(self, expression):
	debug('%s', expression)
        if expression:
            src = dict(format='return ${right}', right=expression)
        else:
            src = dict(format='return')
	self.top.addSource(src)

    def onStatementExpression(self, expr):
        self.top.addSource(expr)

    def onThrow(self, expr):
        stat = self.top.newStatement('raise')
        stat.setExpression(expr)
        return stat

    def onTry(self):
        stat = self.top.newStatement('try')
        self.push(stat)
        return stat

    def onTryExcept(self):
        stat = self.top.newStatement('except')
        self.push(stat)
        return stat

    def onTryExceptClause(self, stat, clause, pop=False):
        src = dict(format='($left, ), $right', left=clause['type'], right=clause['left'])
        stat.setExpression(src)
        return (self.pop() if pop else None)

    def onTryFinally(self):
        stat = self.top.newStatement('finally')
        self.push(stat)
        return stat

    def onVariables(self, variables, applyType=marker):
	debug('%s %s', variables, applyType)
        if applyType is not marker:
            for var in variables:
                var['type'] = applyType
	renames = self.top.config.combined('variableNameMapping')
	for var in variables:
	    name = var.get('left', '?')
	    name = renames.get(name, name)
	    v = self.top.newVariable(name)
	    v.name = name
            src = {'format':'$left = $right', 'left':name, 'right':'', }
	    if 'right' in var:
                src['right'] = var['right']
                v.expr = var['right']
	    else:
                src['format'] += '()'
                src['right'] = var.get('type', 'MissingType')
                v.expr = src['right']
	    self.top.addSource(src)

    def onWhile(self):
        stat = self.top.newStatement('while')
        self.push(stat)
        return stat

    def onWhileFinish(self, stat, expr, pop=False):
        stat.setExpression(expr)
        return (self.pop() if pop else None)

    def pop(self):
        value = self.stack.pop()
        debug('%s', (value.name if hasattr(value, 'name') else value))
	return value

    def push(self, value):
        debug('%s', (value.name if hasattr(value, 'name') else value))
	self.stack.append(value)

    def fixFloatLiteral(self, value):
        if value.startswith('.'):
            value = '0' + value
        if value.endswith(('f', 'd')):
            value = value[:-1]
        elif value.endswith(('l', 'L')):
            value = value[:-1] + 'L'
        return value
