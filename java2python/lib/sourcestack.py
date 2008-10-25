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
	for mod in (mods or []):
	    klass.addModifier(mod)
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

    def onVariables(self, variables):
	print "## onVariables", variables
	for var in variables:
	    name, value = var.get("id", "?"), var.get("init", marker)
	    v = self.current.newVariable(name)
	    v.setName(name)
	    if value is not marker:
		self.current.addSource("%s = %s" % (name, value))

    def onAssign(self, op, left, right):
        #self.source.current.fixAssignInExpr(True, ("\%s = \%s", (left, right)), left)
        self.source.current.addSource("%s %s %s" % (left, op, right))

    def push(self, value):
	self.stack.append(value)

    def pop(self):
	return self.stack.pop()
