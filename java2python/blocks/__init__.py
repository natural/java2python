#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from string import Template
from java2python.config import Config
from java2python.lib.colortools import red, yellow, green, cyan, white


class Block(object):
    def __init__(self, config):
	self.setConfig(config)
	self.setChildren([])
	self.setComments([])
	self.setDecorators([])
	self.setModifiers([])
	self.setName(None)
	self.setParent(None)
	self.setType(None)

    def __str__(self):
	decl = self.getDeclaration()
	decls = [decl] if decl else []
	indent = self.indent()
        lines = ['%s%s' % (indent*o.getDepth(), o) for o in self.getChildren()]
	return unicode.join(u'\n', decls + lines)

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
    # comments accessors
    def getComments(self):
	return self.comments

    def setComments(self, comments):
	self.comments = comments

    def addComment(self, comment):
	start, stop, lines = comment
	for line in lines:
	    e = Comment(config=self.config,
			   format='${left}',
		           left='# %s' % line.rstrip().lstrip('\n'))
	    e.setParent(self)

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
	if isinstance(self.parent, (Module, )):
	    return 0
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
    def cleanup(self):
	self.addChild(Expression(config=self.config, format='\n'))

    def debugFormat(self):
	parts = []
	add = lambda *x:parts.extend(x)
	add(white('<'))
	add(green(self.__class__.__name__))
	add(' ', white('name:'), cyan(self.getName()))
	add(' ', white('type:'), cyan(self.getType() or 'Unknown'))
	mods = self.getModifiers()
	if mods:
	    add(' ', white('mods:'), cyan(', '.join(self.getModifiers())))
	add(white('>'))
	return ''.join(parts)

    def debugPrint(self, level=0):
	indent = ' '*4
	print >> sys.stderr, '%s%s' % (indent*level, self.debugFormat())
	for o in self.getChildren():
	    printer = getattr(o, 'debugPrint', None)
	    if printer:
		printer(level+1)

    def isComment(self):
	return False

    def indent(self):
	return '    ' # make config value

    def isPublic(self):
	return 'public' in self.modifiers

    def isStatic(self):
	return 'static' in self.modifiers

    def isVoid(self):
	return 'void' == self.type

    def reparentChildren(self, target):
	for child in self.getChildren():
	    child.modifiers = self.modifiers
	    child.type = self.type
	    child.setParent(target)
    ##
    def getAtLeastOneChild(self):
	children = self.children[:]
	filtered = [c for c in children if not c.isComment()]
	if not filtered:
	    comment = Expression(self.config, format='${left}', left='pass')
	    comment.setParent(self, autoAdd=False)
	    children.append(comment)
	return children


class Module(Block):
    def __init__(self, config):
	Block.__init__(self, config)
    	self.setPackages([])
    	self.setImports([])

    ##
    # import accessors
    def getImports(self):
	return self.imports

    def setImports(self, values):
	self.imports = values

    def addImport(self, value, isStatic=False, dotStar=False):
	self.imports.append((value, isStatic, dotStar))

    ##
    # package accessors
    def getPackages(self):
	return self.packages

    def setPackages(self, values):
	self.packages = values

    def addPackage(self, value):
	self.packages.append(value)


class Class(Block):
    def __init__(self, config):
	Block.__init__(self, config)
	self.getChildren = self.getAtLeastOneChild

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


class Method(Block):
    def __init__(self, config):
	Block.__init__(self, config)
    	self.setParameters([])
	self.getChildren = self.getAtLeastOneChild

    ##
    # parameter accessors
    def getParameters(self):
	return self.parameters

    def setParameters(self, params):
	self.parameters = params

    def addParameter(self, param):
	self.parameters.append(param)

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
	defaults = dict(left='', right='', format='', comment='')
	defaults.update(kwds)
	self.update(**defaults)

    def __nonzero__(self):
	return bool(self.format)

    def __str__(self):
	template = Template(self.format).safe_substitute
	return template(left=self.left, right=self.right,
			type=self.type, comment=self.comment)

    ##
    # convenience for grammar operations; simpler than assigning
    # multiple attributes
    def update(self, **kwds):
	for key, value in kwds.items():
	    setattr(self, key, value)

    ##
    # methods for simple creation of nested expressions
    def nestLeft(self, **kwds):
	self.left = left = self.new(self.config)
	left.update(**kwds)
	return left

    def nestRight(self, **kwds):
	self.right = right = self.new(self.config)
	right.update(**kwds)
	return right

    @classmethod
    def new(cls, config):
	return cls(config)

    ##
    # base class accessor overrides
    def addComment(self, comment):
	start, stop, lines = comment
	if not self.format.count('${comment}'):
	    self.format = self.format + ' # ${comment}'
	self.comment += ' '.join(lines)

    ##
    # base class utility overrides
    def debugFormat(self, title=''):
	parts = []
	add = lambda *x:parts.extend(x)
	add(white('<'))
	add(green('%s' % (title or self.__class__.__name__)))
	for name in ('format', 'left', 'right', 'type'):
	    attr = getattr(self, name, None)
	    if attr and isinstance(attr, (basestring, )):
		add(' ', white(name+':'), yellow(attr))
	    ## other object types not formatted; debugPrint handles
	    ## them directly.
	add(white('>'))
	return ''.join(parts)

    def debugPrint(self, level=0, title=''):
	indent = ' '*4
	print >> sys.stderr, '%s%s' % (indent*level, self.debugFormat(title))
	for name in ('left', 'right', 'type'):
	    obj = getattr(self, name, None)
	    printer = getattr(obj, 'debugPrint', None)
	    if printer:
		printer(level+1, name.title())


class Comment(Expression):
    def isComment(self):
	return True


class BlockFactory(object):
    ##
    # implemented like this so that it
    # can be manipulated externally.
    types = {
	'block':Block,
	'module':Module,
	'class':Class,
	'method':Method,
	'expression':Expression,
	'comment':Comment,
    }

    def __init__(self, configs):
	self.config = Config(configs)

    def __call__(self, name, **kwds):
	try:
	    cls = self.types[name]
	except (KeyError, ):
	    raise TypeError('Unknown factory type: %s' % (name, ))
	return cls(self.config, **kwds)
