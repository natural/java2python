#!/usr/bin/env python
from logging import debug
from java2python import ev, marker

## javadoc handler
## enums
## annos
## arrays
## statements
## diff testing

class BlockStack:
    """ A simple stack of source blocks.

    """
    def __init__(self, module):
	self.stack = [module]

    def bottom(self):return self.stack[0]
    bottom = property(bottom)

    def top(self):return self.stack[-1]
    top = property(top)

    def onBsr(self, left, right):
        handler = self.top.config.handler('bsrHandler')
        return handler(self, left, right)

    def onBsrAssign(self, left, right):
        handler = self.top.config.handler('bsrHandlerAssign')
        return handler(self, left, right)

    def altId(self, value):
	alt = self.top.config.combined('identRenames')
        return alt.get(value, value)

    def altType(self, value):
        alt = self.top.config.combined('typeRenames')
        return alt.get(value, value)

    def makeArrayCreator(self, typ, ctor):
        ## it can't be this easy
        value = dict(left=typ, right=ctor, format='[$left() for _ in range($right)]')
        return value

    def makeParamDecl(self, decl, typ, isVariadic=False):
        debug('%s %s %s', decl, typ, isVariadic)
        new = decl.copy()
        new.update(type=typ, format='$left',
                   left=ev('*' if isVariadic else '', decl, '$left$right'))
        debug('%s', new)
        return new

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
        stat = self.top.makeStatement('assert')
        stat.setExpression(src)

    def onAssign(self, op, left, right):
        debug('%s %s %s', op, left, right)
        src = ev(left, right, '$left %s $right' % op)
        self.top.addSource(src)

    def onBreak(self, label):
        debug('%s', label)
        label = self.altId(label)
        ## ident doesn't need expression formatting, so we add the
        ## string directly.  same true below for the 'continue'
        ## statement.
        self.top.addSource('break' + (' #label:' + label if label else ''))

    def onClass(self, name, mods=None, extends=None, implements=None):
	debug('%s %s %s %s', name, mods, extends, implements)
        name = self.altId(name)
	klass = self.top.makeClass()
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
        label = self.altId(label)
        self.top.addSource('continue' + (' # ' + label if label else ''))

    def onDo(self):
        debug('')
        stat = self.top.makeStatement('while')
        stat.setExpression('True')
        self.push(stat)
        return stat

    def onDoFinish(self, stat, expr, pop=False):
        debug('%s %s %s', stat, expr, pop)
        ifstat = stat.makeStatement('if')
        ifstat.makeStatement('break')
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
        for handler in self.top.config.handlers('enumConstantHandlers'):
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

    def onIf(self, expr):
        debug('%s', expr)
        ifstat, elsestat = self.top.makeIf()
        rexpr = expr.copy()
        rexpr['format'] = '$left' # don't need parens in python if-statements
        ifstat.expr = rexpr
        self.push(ifstat)
        return ifstat, elsestat

    def onSwitch(self, expr):
        debug('%s', expr)
        switchstat, elsestat = self.top.makeIf()
        switchstat.expr = expr
        self.push(switchstat)
        return switchstat

    def onSwitchCase(self, expr):
        last = self.top
        last.expr = expr
        self.pop()
        elsestat = self.top.makeStatement('elif')
        elsestat.expr = last.expr
        self.push(elsestat)

    def onSwitchDefault(self):
        pass

    def onSync(self, expr):
        debug('%s', expr)
        syncstat = self.top.makeStatement('with')
        syncstat.expr = ev(right=expr, format='exlock($right)')
        self.push(syncstat)
        return syncstat

    def onFor(self, expressions, condition):
        debug('%s %s', expressions, condition)
        blk, stat = self.top.makeFor()
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
        ident = self.altId(ident)
        blk, stat = self.top.makeForEach()
        src = ev(ident, exp, '$left in $right')
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
        for handler in self.top.config.handlers('importHandlers'):
            handler(self, decl, isStatic, isStar)
        return decl

    def onMethod(self, name, mods=None, params=None, typ=None, pop=False):
	debug('%s %s %s', name, mods, params)
        name = self.altId(name)
	meth = self.top.makeMethod()
	meth.name = name
        meth.type = typ
	for mod in (mods or []):
	    meth.addModifier(mod)
	for param in (params or []):
	    #if len(param) == 2:
	    #    param += [None]
	    t, p, a = param.get('type', ''), param.get('left', ''), param.get('array')
            p = meth.formatExpression(p)
	    meth.addParameter(t, p)
	self.push(meth)
        return (self.pop() if pop else meth)

    def onPackageDecl(self, decl):
        debug('%s', decl)
        for handler in self.top.config.handlers('packageHandlers'):
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
        stat = self.top.makeStatement('raise')
        stat.setExpression(expr)
        return stat

    def onTry(self):
        stat = self.top.makeStatement('try')
        self.push(stat)
        return stat

    def onTryExcept(self):
        stat = self.top.makeStatement('except')
        self.push(stat)
        return stat

    def onTryExceptClause(self, stat, clause, pop=False):
        src = dict(format='($left, ), $right', left=clause['type'], right=clause['left'])
        stat.setExpression(src)
        return (self.pop() if pop else None)

    def onTryFinally(self):
        stat = self.top.makeStatement('finally')
        self.push(stat)
        return stat

    def onLocalDecls(self, decls, typ):
        debug('%s %s', decls, typ)
        for decl in decls:
            if 'right' in decl and not decl['right']:
                renames = self.top.config.combined('typeRenames')
                try:
                    rtyp = renames.get(typ, typ)
                except (TypeError, ):
                    rtyp = typ
                decl['right'] = ev(rtyp, format='$left()')
            name = decl.get('left', None)
            right = decl.get('right', None)
            if name is None or right is None:
                continue
            src = ev(name, right, '$left = $right')
            self.top.addSource(src)

    def onVariables(self, decls, applyType=marker):
	debug('%s %s', decls, applyType)
        if applyType is not marker:
            for decl in decls:
                ## need to specify "type()" not just "type" ??
                #decl['right'] = applyType
                if not decl['right']:
                    decl['right'] = applyType
                decl['type'] = applyType
	#renames = self.top.config.combined('identRenames')
        renames = {}
	for decl in decls:
	    name = decl.get('left', '?')
	    name = renames.get(name, name)
	    var = self.top.addVariable(name, True)
            src = {'format':'$left = $right', 'left':name, 'right':'', }
	    if 'right' in decl:
                src['right'] = decl['right']
                var.expr = decl['right']
	    else:
                src['format'] += '()'
                src['right'] = decl.get('type', 'MissingType')
                var.expr = src['right']
	    self.top.addSource(src)

    def onWhile(self):
        stat = self.top.makeStatement('while')
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
