#!/usr/bin/env python


marker = object()


class SimplePythonSourceStack(object):
    def __init__(self, module):
	self.stack = [module]

    def get_current(self):
	return self.stack[-1]
    current = property(get_current)


    def onPackageDecl(self, name):
	self.current.addComment("namespace_packages('%s')" % name)


    def onImportDecl(self, name, isStatic, isStar):
	if isStatic:
	    if isStar:
		c = "from %s import *" % name
	    else:
		names = name.split('.')
		c = "from %s import %s" % (str.join('.', names[:-1]), names[-1])
	else:
	    c = "import %s" % name
	self.current.addComment(c)


    def onClass(self, name, mods=None, extends=None, implements=None):
	print "## onClass", name, mods, extends, implements
	klass = self.current.newClass()
	klass.setName(name)

	def annoDecl(v):
	    s = []
	    for d in v:
		for k in d:
		    if len(k) == 2:
			s.append("%s=%s" % tuple(k))
		    else:
			s.append(k)
	    return ", ".join(s)

	for mod in (mods or []):
	    if isinstance(mod, basestring):
                klass.addModifier(mod)
	    elif isinstance(mod, list):
		name, inits = mod
		if inits:
		    suffix = "(" + annoDecl(inits) +  ")"
		else:
		    suffix = ""
		name += suffix
		## check 2vs3 and adjust -- class decos not supported in 2.x.
		klass.addModifier("@" + name)

	for base in (extends or []) + (implements or []):
	    klass.addBaseClass(base)
	self.push(klass)
	return klass

    def onMethod(self, name, mods=None, params=None):
	print "## onMethod", name, mods, params
	meth = self.current.newMethod()
	meth.setName(name)
	for mod in (mods or []):
	    meth.addModifier(mod)
	for param in (params or []):
	    #if len(param) == 2:
	    #    param += [None]
	    t, p, a = param.get('type', ''), param.get('id', ''), param.get('array')
	    meth.addParameter(t, p)
	self.push(meth)
	return meth

    def onAnnotationMethod(self, name, annodecls, default):
	meth = self.onMethod(name)
	for annodecl in (annodecls or []):
            meth.addModifier(annodecl[0])
	if default:
	    src = "return %s" % (default, )
	else:
	    src = "pass"
        meth.addSource(src)
	self.pop()
	return meth


    def makeMethodExpr(self, pex, args):
	print "## makeMethodExpr", pex, args
        src = str(pex or "None") + "(" + str.join(", ", [str(a or "") for a in args]) + ")"
	return src
	#self.current.addSource(src)

    def onVariables(self, variables):
	print "## onVariables", variables
	renames = self.current.config.combined('variableNameMapping')
	for var in variables:
	    name, value = var.get("id", "?"), var.get("init", marker)
	    name = renames.get(name, name)
	    v = self.current.newVariable(name)
	    v.setName(name)

	    if 'init' in var:
		src = "%s = %s" % (name, value)
	    else:
		src = "%s = %s()" % (name, var.get('type'))
	    self.current.addSource(src)


    def onAssign(self, op, left, right):
        #self.source.current.fixAssignInExpr(True, ("\%s = \%s", (left, right)), left)
        #self.current.addSource("%s %s %s" % (left, op, right))
	pass

    def onReturn(self, pex):
	print "## onReturn", pex
	src = ("return %s", pex) if pex else "return"
	self.current.addSource(src)

    def push(self, value):
	self.stack.append(value)

    def pop(self):
	return self.stack.pop()


    def altName(self, name):
	return self.current.fixDecl(name)


    def onEnumScope(self, enums):
	print "## onEnumScope", enums


    def onEnum(self, name, values):
	klass = self.onClass(name)
	klass.addBaseClass('EnumValue')
	return klass


    def onAnnoType(self, name, modifiers):
	## lookup base class
	bases = ['object', ]
	klass = self.onClass(name, [], bases)
	return klass
