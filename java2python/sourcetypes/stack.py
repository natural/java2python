#!/usr/bin/env python
from logging import debug

## yes, one of those.
marker = object()


class SimplePythonSourceStack(object):
    def __init__(self, module):
	self.stack = [module]

    def get_current(self):
	return self.stack[-1]
    current = property(get_current)

    def onPackageDecl(self, name):
        debug('%s', name)
	self.current.addComment("namespace_packages('%s')" % name)

    def onImportDecl(self, name, isStatic, isStar):
        debug('%s %s %s', name, isStatic, isStar)
	if isStatic:
	    if isStar:
		c = 'from %s import *' % name
	    else:
		names = name.split('.')
		c = 'from %s import %s' % (str.join('.', names[:-1]), names[-1])
	else:
	    c = 'import %s' % name
	self.current.addComment(c)

    def onBreak(self, label):
        debug('%s', label)
        self.current.addSource('break' + (' #label:' + label if label else ''))

    def onContinue(self, label):
        debug('%s', label)
        self.current.addSource('continue' + (' # ' + label if label else ''))

    def onClass(self, name, mods=None, extends=None, implements=None):
	debug('%s %s %s %s', name, mods, extends, implements)
	klass = self.current.newClass()
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
		name += suffix
		klass.addModifier('@' + name)

	for base in (extends or []) + (implements or []):
	    klass.addBaseClass(base)
	self.push(klass)
	return klass

    def onForEach(self, typ, ident, exp):
        debug('%s %s %s', typ, ident, exp)
        blk, stat = self.current.newForEach()
        stat.setExpression('%s in %s' % (ident, exp))
        self.push(stat)
        return blk, stat

    def onFor(self, expressions, condition):
        debug('%s %s', expressions, condition)
        blk, stat = self.current.newFor()
        #for expr in expressions:
        #    self.current.addSource(expr)
        if condition is None:
            condition = 'True'
        stat.setExpression(condition)
        stat.addSource('pass')
        self.push(stat)
        return blk, stat

    def onForFinish(self, stat, updates, pop=False):
        for update in updates:
            stat.addSource(update)
        return (self.pop() if pop else None)

    def onDo(self):
        debug('')
        stat = self.current.newStatement('while')
        stat.setExpression('True')
        self.push(stat)
        return stat

    def onDoFinish(self, stat, expr, pop=False):
        debug('%s %s %s', stat, expr, pop)
        ifstat = stat.newStatement('if')
        ifstat.newStatement('break')
        ifstat.setExpression('not %s' % expr)
        return (self.pop() if pop else None)

    def onWhile(self):
        stat = self.current.newStatement('while')
        self.push(stat)
        return stat

    def onWhileFinish(self, stat, expr, pop=False):
        stat.setExpression(expr)
        return (self.pop() if pop else None)

    def onThrow(self, expr):
        stat = self.current.newStatement('raise')
        stat.setExpression(expr)
        return stat

    def onMethod(self, name, mods=None, params=None, pop=False):
	debug('%s %s %s', name, mods, params)
	meth = self.current.newMethod()
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

    def onAnnotationMethod(self, name, annodecls, default):
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


    def makeParamDecl(self, src, typ, isVariadic=False):

        exp = src.copy()
        exp['type'] = typ
        exp['fmt'] = '$left'
        if isVariadic:
            exp['id'] = '*' + exp['id']
        debug('(return value) %s %s %s', exp, typ, isVariadic)
        return exp

    def makeMethodExpr(self, pex, args):
	debug('%s %s', pex, args)
        args = [dict(fmt="$left", left=arg) for arg in args]
        return dict(left=pex, right=args, fmt='$left($right)')
        return ('%s(%s)', (pex, args, ))
        src = str(pex or 'None') + '(' + str.join(', ', [str(a or '') for a in args]) + ')'
	return src
	#self.current.addSource(src)

    def onVariables(self, variables, applyType=marker):
	debug('%s %s', variables, applyType)
        if applyType is not marker:
            for var in variables:
                var['type'] = applyType
	renames = self.current.config.combined('variableNameMapping')
	for var in variables:
	    name = var.get('left', '?')
	    name = renames.get(name, name)
	    v = self.current.newVariable(name)
	    v.name = name
            src = {'id':name, 'fmt':'', 'left':'', 'right':'', }
	    if 'right' in var:
                src['fmt'] = '$left = $right'
                src['left'] = src['id']
                src['right'] = var['right']
	    else:
		#src = ('%s = %s()', (name, var.get('type')))
                src['fmt'] = '$id = $val()'
                src['right'] = '^^^'
	    self.current.addSource(src)


    def onAssign(self, op, left, right):
        #self.source.current.fixAssignInExpr(True, ('\%s = \%s', (left, right)), left)
        debug('%s %s %s', op, left, right)
        self.current.addSource('%s %s %s' % (left, op, right))

    def onReturn(self, pex):
	debug('%s', pex)
	src = ('return %s', pex) if pex else 'return'
	self.current.addSource(src)

    def push(self, value):
        debug('%s', (value.name if hasattr(value, 'name') else value))
	self.stack.append(value)

    def pop(self):
        value = self.stack.pop()
        debug('%s', (value.name if hasattr(value, 'name') else value))
	return value


    def altName(self, name):
	return self.current.fixDecl(name)

    def onEnum(self, name, mods=None, implements=None):
        debug('%s', name)
	klass = self.onClass(name)
        #from java2python.config.enumhandlers import minjava
        #minjava(self)
	return klass

    def onEnumConstant(self, decl):
        name = decl['id']
        debug('%s', name)

        if not name.startswith('<missing'):
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

    def onAnnoType(self, name, modifiers):
	## lookup base class
	bases = ['object', ]
	klass = self.onClass(name, [], bases)
	return klass

    def fixFloatLiteral(self, value):
        if value.startswith('.'):
            value = '0' + value
        if value.endswith(('f', 'd')):
            value = value[:-1]
        elif value.endswith(('l', 'L')):
            value = value[:-1] + 'L'
        return value


    def makeArrayAccess(self, pri, exp):
        return '%s[%s]' % (pri, exp, )


    def onAssert(self, exp, arg=marker):
        debug('%s %s', exp, arg)
        if arg is not marker:
            src = 'assert %s, %s' % (exp, arg, )
            s = self.current.newStatement(src)
        else:
            src = 'assert %s' % (exp, )
            s = self.current.newStatement(src)
            #s.setExpression(exp)

    def onTry(self):
        stat = self.current.newStatement('try')
        self.push(stat)
        return stat

    def onExcept(self):
        stat = self.current.newStatement('except')
        self.push(stat)
        return stat

    def onExceptClause(self, stat, clause, pop=False):
        exc = clause.get('type')
        nam = clause.get('id')
        src = '(%s, ), %s' % (exc, nam)
        stat.setExpression(src)
        return (self.pop() if pop else None)

    def onFinally(self):
        stat = self.current.newStatement('finally')
        self.push(stat)
        return stat
