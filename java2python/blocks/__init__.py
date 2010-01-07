#!/usr/bin/env python
from string import Template
from java2python.config import Config


class Block(object):
    def __init__(self, config):
	self.setConfig(config)
	self.setChildren([])
	self.setDecorators([])
	self.setModifiers([])
	self.setName(None)
	self.setParameters([])
	self.setParent(None)
	self.setType(None)

    def __str__(self):
	decl = self.getDeclaration()
	decls = [decl] if decl else []
	indent = self.indent()
        lines = ['%s%s' % (indent*o.getDepth(), o) for o in self.children]
	return ('\n').join(decls + lines)

    def __repr__(self):
	v = '<%s name:%s type:%s modifiers:%s>'
	clsname = self.__class__.__name__
	objname = self.getName()
	typname = self.getType()
	mods = ', '.join(self.getModifiers()) if self.getModifiers() else []
	return v % (clsname, objname, typname, mods)

    def setConfig(self, config):
	self.config = config

    def getDeclaration(self):
	return None

    ##
    # children accessors
    def getChildren(self):
	return self.children

    def setChildren(self, children):
	self.children = children

    def addChild(self, obj):
	self.children.append(obj)

    ##
    # decorator accessors
    def getDecorators(self):
	return self.decorators

    def setDecorators(self, decorators):
	self.decorators = decorators

    def addDecorator(self, decorator):
	self.decorators.append(decorator)

    ##
    # modifier accessors
    def getModifiers(self):
	return self.modifiers

    def setModifiers(self, modifiers):
	self.modifiers = modifiers

    def addModifier(self, modifier):
	self.modifiers.append(modifier)

    ##
    # name accessors
    def getName(self):
	return self.name

    def setName(self, value):
	self.name = value

    ##
    # parameter accessors
    def getParameters(self):
	return self.parameters

    def setParameters(self, params):
	self.parameters = params

    def addParameter(self, param):
	self.parameters.append(param)

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
    def getType(self, asString=True):
	value = getattr(self, 'type', None)
	if isinstance(value, (basestring, )):
	    return value
	if isinstance(value, (tuple, list, )) and asString:
	    return '.'.join(self.type)
	return value

    def setType(self, value):
	self.type = value

    ##
    # calculates the depth of this block based on the number of
    # parents
    def getDepth(self):
	depth = 0
	while self:
	    if self.parent:
		self = self.parent
		depth += 1
	    else:
		return depth
	return depth

    ##
    # utilities
    def debugPrint(self):
	print '%s %s%r' % ('#', self.indent()*self.getDepth(), self)
	for o in self.children:
	    o.debugPrint()

    def indent(self):
	return '    ' # make config value

    def isPublic(self):
	return 'public' in self.modifiers

    def isStatic(self):
	return 'static' in self.modifiers


    def isVoid(self):
	return 'void' == self.type

    def reparentChildren(self, target):
	for child in self.children:
	    child.modifiers = self.modifiers
	    child.type = self.type
	    child.setParent(target)


class Module(Block):
    pass


class Class(Block):
    ##
    # format and return a class declaration.
    def getDeclaration(self):
	types = ', '.join(self.type or ['object']) # make config
	types = '(%s)' % types if types else ''
	return 'class %s%s:' % (self.name, types)

    ##
    # override the type setter to account for extends or
    # implements clauses
    def setType(self, value):
	if not hasattr(self, 'type'):
	    self.type = []
	if isinstance(value, (tuple, list)):
	    self.type.extend(value)
	elif value:
	    self.type.append(value)

    ##
    # override the depth calculation to make module-level classes
    # appear without indentation.
    def getDepth(self):
	if isinstance(self.parent, (Module, )):
	    return 0
	else:
	    return Block.getDepth(self)

class Method(Block):
    ##
    # format and return a method declaration.
    def getDeclaration(self):
	first = 'cls' if self.isStatic() else 'self'
	params = ', '.join([first] + [str(p) for p in self.getParameters()])
	lines = ['@'+deco for deco in self.getDecorators()]
	lines.append('def %s(%s):' % (self.name, params))
	return ''.join(lines)


class Expression(Block):
    def __init__(self, config, **kwds):
	Block.__init__(self, config)
	defaults = dict(left='', right='', format='')
	defaults.update(kwds)
	self.update(**defaults)

    def __nonzero__(self):
	return bool(self.format)

    def __repr__(self):
	v = '<%s format:%s left:%r right:%r%s%s>'
	t = ' type:%s' % self.type if self.type else ''
	m = ' mods:%s' % ','.join(self.modifiers) if self.modifiers else ''
	c = self.__class__.__name__
	return v % (c, self.format, self.left, self.right, t, m, )

    def __str__(self):
	template = Template(self.format).safe_substitute
	return template(left=self.left, right=self.right, type=self.type)

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
