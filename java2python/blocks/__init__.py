#!/usr/bin/env python
from java2python.config import Config


class Block(object):
    def __init__(self, config):
	self.setConfig(config)
	self.setChildren([])
	self.setModifiers([])
	self.setName(None)
	self.setParent(None)
	self.setType(None)

    def setConfig(self, config):
	self.config = config

    ##
    # children accessors
    def getChildren(self):
	return self.children

    def setChildren(self, children):
	self.children = children

    def addChild(self, obj):
	self.children.append(obj)

    ##
    # name accessors
    def getName(self):
	return self.name

    def setName(self, value):
	self.name = value

    ##
    # parent accessors
    def getParent(self):
	return self.parent

    def setParent(self, parent, autoAdd=True):
	self.parent = parent
	if autoAdd and hasattr(parent, 'addChild'):
	    parent.addChild(self)

    ##
    # type accessors
    def getType(self):
	return self.type

    def setType(self, value):
	self.type = value

    ##
    # modifier accessors
    def getModifiers(self):
	return self.modifiers

    def setModifiers(self, modifiers):
	self.modifiers = modifiers

    def addModifier(self, modifier):
	self.modifiers.append(modifier)

    ##
    # calculates the indentation for this block based on the number of
    # parents
    def indents(self):
	levels = 0
	while self:
	    parent = self.parent
	    if parent:
		self = parent
		levels += 1
	    else:
		return levels

    def __str__(self):
	decl = self.getDecl()
	decl = [decl] if decl else []
        lines = decl + [str(o) for o in self.children]
        return ('\n' + '    ' * self.indents()).join(lines)

    def getDecl(self):
	return None

    def getDecos(self):
	return []

    @property
    def isStatic(self):
	return 'static' in self.modifiers

    @property
    def isPublic(self):
	return 'public' in self.modifiers

    @property
    def isVoid(self):
	return 'void' == self.type


class Module(Block):
    pass


class Class(Block):
    def __init__(self, config):
	Block.__init__(self, config)
	self.setBases([])

    def getDecl(self):
	i = 0 if  isinstance(self.parent, (Module, )) else self.indents()
	bases = ', '.join(self.bases)
	bases = '('+bases+')' if bases else ''
	return ('    ' * i) + 'class %s%s:' % (self.name, bases)

    ##
    # base type for extends or implements clauses
    def getBases(self):
	return self.bases

    def setBases(self, bases):
	self.bases = bases

    def addBase(self, base):
	## base is a list that should be in (translated) dotted notation
	self.bases.extend(base)


class Method(Block):
    def __init__(self, config):
	Block.__init__(self, config)
	self.parameters = []

    def getDecl(self):
 	i = self.indents()
	first = 'cls' if self.isStatic else 'self'
	params = ', '.join([first] + self.parameters)
	decos = '\n'.join(self.getDecos())
	return decos + '\n'+('    '*i) + 'def %s(%s):' % (self.name, params)

    ##
    # parameter accessors
    def getParams(self):
	return self.parameters

    def setParams(self, params):
	self.parameters = params

    def addParam(self, param):
	self.parameters.append(param)

    def getDecos(self):
 	i = self.indents()
	decos = []
	if self.isStatic:
	    decos.append('classmethod')
	return [('    '*i)+'@'+deco for deco in decos]



class BlockFactory(object):
    def __init__(self, configs):
	self.config = Config(configs)

    def __call__(self, name):
	try:
	    cls = globals()[name.title()]
	except (KeyError, ):
	    raise TypeError('Unknown factory type: %s' % (name, ))
	return cls(self.config)
