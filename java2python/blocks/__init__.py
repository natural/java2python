#!/usr/bin/env python
from string import Template
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

    def reparentChildren(self, target):
	for child in self.children:
	    child.modifiers = self.modifiers
	    child.type = self.type
	    child.setParent(target)

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

    def debugPrint(self):
	prefix = '#'
	indent = self.indent
	print '%s %s%r' % (prefix, indent*self.depth(), self)
	for o in self.children:
	    o.debugPrint()

    def __str__(self):
	decl = self.getDecl()
	decls = [decl] if decl else []
	indent = self.indent
        lines = ['%s%s' % (indent*o.depth(), o) for o in self.children]
	return ('\n').join(decls + lines)

    def __repr__(self):
	v = '<%s name:%s type:%s modifiers:%s>'
	clsname = self.__class__.__name__
	objname = self.getName()
	typname = self.getType()
	mods = ', '.join(self.getModifiers()) if self.getModifiers() else []
	return v % (clsname, objname, typname, mods)

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

    @property
    def indent(self):
	return '    ' # make config value

    ##
    # calculates the depth of this block based on the number of
    # parents
    def depth(self):
	depth = 0
	while self:
	    if self.parent:
		self = self.parent
		depth += 1
	    else:
		return depth
	return depth


class Module(Block):
    pass


class Class(Block):
    def __init__(self, config):
	Block.__init__(self, config)

    def getDecl(self):
	#debug('%r', self)
	types = ', '.join(self.type or ['object']) # make config
	types = '(%s)' % types if types else ''
	return 'class %s%s:' % (self.name, types)

    ##
    # override the type setter for extends or implements clauses
    def setType(self, value):
	if not hasattr(self, 'type'):
	    self.type = []
	if isinstance(value, (tuple, list)):
	    self.type.extend(value)
	elif value:
	    self.type.append(value)

    def depth(self):
	if isinstance(self.parent, (Module, )):
	    return 0
	else:
	    return Block.depth(self)

class Method(Block):
    def __init__(self, config):
	Block.__init__(self, config)
	self.parameters = []

    def getDecl(self):
	first = 'cls' if self.isStatic else 'self'
	params = ', '.join([first] + [str(p) for p in self.getParams()])
	lines = ['@'+deco for deco in self.getDecos()]
	lines.append('def %s(%s):' % (self.name, params))
	return ''.join(lines)

    ##
    # parameter accessors
    def getParams(self):
	return self.parameters

    def setParams(self, params):
	self.parameters = params

    def addParam(self, param):
	self.parameters.append(param)


class Expression(Block):
    def __init__(self, config, **kwds):
	Block.__init__(self, config)
	defaults = dict(left='', right='', format='')
	defaults.update(kwds)
	self.update(**defaults)

    def __repr__(self):
	v = '<%s format:%s left:%r right:%r%s%s>'
	t = ' type:%s' % self.type if self.type else ''
	m = ' mods:%s' % ','.join(self.modifiers) if self.modifiers else ''
	c = self.__class__.__name__
	return v % (c, self.format, self.left, self.right, t, m, )

    def __str__(self):
	template = Template(self.format).safe_substitute
	return template(left=self.left, right=self.right, type=self.type)

    def __nonzero__(self):
	return bool(self.format)
	#return all((self.left, self.format))
	#return any((self.left, self.right, self.format))

    def nestLeft(self, **kwds):
	self.left = left = self.new(self.config)
	left.update(**kwds)
	return left

    def nestRight(self, **kwds):
	self.right = right = self.new(self.config)
	right.update(**kwds)
	return right

    def update(self, **kwds):
	for key, value in kwds.items():
	    setattr(self, key, value)

    @classmethod
    def new(cls, config):
	return cls(config)


class BlockFactory(object):
    def __init__(self, configs):
	self.config = Config(configs)

    def __call__(self, name, **kwds):
	try:
	    cls = globals()[name.title()]
	except (KeyError, ):
	    raise TypeError('Unknown factory type: %s' % (name, ))
	return cls(self.config, **kwds)
