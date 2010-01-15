#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools
import keyword
import sys
import StringIO

import java2python.lib.colortools as color


class Block(object):
    """ Block -> basic block of Python code.

    """
    keywords = keyword.kwlist + ['None', 'str', ]

    def __init__(self, config):
	self.setConfig(config)
	self.setChildren([])
	self.setDecorators([])
	self.setModifiers([])
	self.setName(None)
	self.setParent(None)
	self.setType(None)
	self.setVariables([])

    @classmethod
    def className(cls):
	""" Returns the name of this class.

	"""
	return cls.__name__

    @classmethod
    def new(cls, config, **kwds):
	""" Creates a block of this type and with this config.

	"""
	return cls(config, **kwds)

    ##
    # default iteration methods

    def iterPrologue(self):
	""" Default implementation of prologue line iterator; yields None.

	"""
	yield None

    def iterChildren(self):
	""" Default child iterator implementation; yields each child block.

	"""
	return iter(self.getChildren())

    ##
    # default accessors

    def getChildren(self):
	""" Returns sequence of children for this block.

	"""
	return self.children

    def setChildren(self, value):
	""" Sets the children of this block to the given value.

	"""
	self.children = value

    def addChild(self, value):
	""" Adds a child to this block.

	"""
	self.children.append(value)

    def addComment(self, comment):
	""" Places comments at the end of this block.

	"""
	start, stop, lines = comment
	prefix = self.getCommentPrefix()
	for line in lines:
	    comment = '{0}{1}'.format(prefix, line.rstrip().lstrip('\n'))
	    expr = Comment(config=self.getConfig(), format=comment)
	    expr.setParent(self)

    def getConfig(self):
	""" Returns the configuration object for this block.

	"""
	return self.config

    def setConfig(self, config):
	""" Sets the configuration object for this block.

	"""
	self.config = config

    def getDecorators(self):
	""" Returns the decorators of this block.

	"""
	return self.decorators

    def setDecorators(self, value):
	""" Sets the decorators of this block.

	"""
	self.decorators = value

    def addDecorator(self, value):
	""" Adds a decorator to this block.

	"""
	self.decorators.append(value)

    def getModifiers(self):
	""" Returns the modifiers of this block.

	"""
	return self.modifiers

    def setModifiers(self, value):
	""" Sets the modifiers of this block.

	"""
	self.modifiers = value

    def addModifier(self, value):
	""" Adds a modifier to this block.

	"""
	self.modifiers.append(value)

    def getName(self):
	""" Returns the name of this block.

	"""
	return self.name

    def setName(self, value):
	""" Sets the name of this block.

	"""
	self.name = value

    def getParent(self):
	""" Returns the parent of this block.

	"""
	return self.parent

    def setParent(self, parent, autoAdd=True):
	""" Sets the parent of this block.

	"""
	self.parent = parent
	if autoAdd and hasattr(parent, 'addChild'):
	    parent.addChild(self)

    def getType(self, separator='.'):
	""" Returns the type of this block.

	"""
	value = getattr(self, 'type', None)
	if isinstance(value, (basestring, )):
	    return value
	elif isinstance(value, (tuple, list, )) and separator:
	    return separator.join(self.type)
	else:
	    return value

    def setType(self, value):
	""" Sets the type of this block.

	"""
	self.type = value

    def getVariables(self):
	""" Returns the variable sequence of this block.

	"""
	return self.variables

    def setVariables(self, value):
	""" Sets the variable sequence of this block to the given value.

	"""
	self.variables = value

    def addVariable(self, value):
	""" Adds the given value to the variable sequence of this block.

	"""
	self.variables.append(value)

    def getIndent(self, default='    '):
	""" Returns the configured indent character(s) or the default.

	"""
	return self.getConfig().last('leadingIndent', default)

    def getCommentPrefix(self, default='# '):
	""" Returns the configured comment prefix or the default.

	"""
	return self.getConfig().last('commentPrefix', default)

    ##
    # output methods

    def dump(self, fd, level=0):
	""" dump(fd, [level]) -> prints this block to the given file-like object.

	"""
	indent = level * self.getIndent()
	notnone = lambda x:x is not None
	for line in itertools.ifilter(notnone, self.iterPrologue()):
	    print >> fd, '{0}{1}'.format(indent, line)
	for child in self.iterChildren():
	    child.dump(fd, level+1)

    def debugFormat(self):
	""" Returns a formatted (maybe with color) string for this block.

	"""
	parts = []
	add = lambda *x:parts.extend(x)
	add(color.white('<'), color.green(self.className()))
	add(' ', color.white('name:'), color.cyan(self.getName()))
	add(' ', color.white('type:'), color.cyan(self.getType() or 'Unknown'))
	mods = self.getModifiers()
	if mods:
	    add(' ', color.white('mods:'), color.cyan(', '.join(mods)))
	add(color.white('>'))
	return ''.join(parts)

    def debugPrint(self, level=0):
	""" Prints the formatted string for this object to stderr.

	"""
	indent = self.getIndent()
	print >> sys.stderr, '{0}{1}'.format(indent*level, self.debugFormat())
	for child in [o for o in self.getChildren() if o]:
	    printer = getattr(child, 'debugPrint', lambda v:None)
	    printer(level+1)

    ##
    # utilities
    isClass = False
    isMethod = False
    isComment = False

    @property
    def isPublic(self):
	""" True if this block has a 'public' modifier.

	"""
	return 'public' in self.modifiers

    @property
    def isStatic(self):
	""" True if this block has a 'static' modifier.

	"""
	return 'static' in self.modifiers

    @property
    def isVoid(self):
	""" True if the type of this block is 'void'.

	"""
	return 'void' == self.type

    def reparentChildren(self, target):
	""" Moves children of this block to target; adjusts types and parent.

	"""
	for child in self.getChildren():
	    child.setModifiers(self.modifiers)
	    child.setType(self.type)
	    child.setVariables(self.variables)
	    child.setParent(target)

    def update(self, **kwds):
	"""  Keyword-based attribute assignment; convenience for the grammar.

	"""
	for key, value in kwds.items():
	    setattr(self, key, value)

    def altName(self, value):
	if value in self.keywords:
	    value = '{0}_'.format(value)
	return value

    def getHandler(self, value):
	name = '{0}{1}'.format(self.className().lower(), value)
	return self.getConfig().handler(name)

    def getHandlers(self, value):
	name = '{0}{1}'.format(self.className().lower(), value)
	return self.getConfig().handlers(name, all=True)


class Module(Block):
    """ Module -> type of block for Python modules.

    """
    def __init__(self, config):
	Block.__init__(self, config)
    	self.setPackages([])
    	self.setImports([])

    def __str__(self):
	""" Returns generated python source code for this Module.

	"""
	strfd = StringIO.StringIO()
	self.dump(strfd, -1)
	source = strfd.getvalue() + '\n'
	for handler in self.getHandlers('OutputHandlers'):
	    source = handler(self, source)
	return source


    def getImports(self):
	""" Returns sequence of imports for this module.

	"""
	return self.imports

    def setImports(self, value):
	""" Sets the sequence of imports for this module.

	"""
	self.imports = value

    def addImport(self, value, static=False, star=False):
	""" Adds an import to this module.

	"""
	self.imports.append((value, static, star))

    def getPackages(self):
	""" Returns sequence of package statements for this module.

	"""
	return self.packages

    def setPackages(self, value):
	""" Sets the sequence of package statements for this module.

	"""
	self.packages = value

    def addPackage(self, value):
	""" Adds a package statement to this module.

	"""
	self.packages.append(value)

    def cleanup(self):
	""" Grammar helper called after parsing.

	TODO:  make this a configuration epilogue
	"""
	#self.addChild(Expression(config=self.getConfig(), format='\n'))

    def iterPrologue(self):
	""" iterPrologue -> yields module prologue lines by calling config handlers.

	"""
	for handler in self.getHandlers('PrologueHandlers'):
	    for line in handler(self):
		yield line



class PostDeclDocString(object):
    """ PostDeclDocString -> mixin for optional docstring and
        automatic 'pass' statement on empty blocks.

	At a minimum, classes and methods must have either a docstring
	or one expression or statement.  The iterChildren method in
	this mixin accounts for this by first calling the docstring
	handlers for the block and then checking for at least one
	non-comment child.
    """
    def iterChildren(self):
	children = []
	handlers = self.getHandlers('DocStringHandlers')
	for doc in itertools.chain(*(handler(self) for handler in handlers)):
	    children.append(Expression(self.getConfig(), format=doc))
	children += self.getChildren()
	filtered = [c for c in children if not c.isComment]
	if not filtered:
	    children.append(Expression(self.getConfig(), format='pass'))
	return iter(children)


class Class(PostDeclDocString, Block):
    """ Class -> type of block for Python classes.

    """
    isEnum = False
    isClass = True

    def __init__(self, config):
	Block.__init__(self, config)
	self.setEnumConstants([])

    def iterPrologue(self):
	""" Returns the declaration for this class.

	"""
	handler = self.getHandler('BaseLookup')
	bases = [b for b in handler(self) if b is not None]
        bases = '({0})'.format(', '.join(bases)) if bases else ''
	yield 'class {0}{1}:'.format(self.getName(), bases)

    def setType(self, value):
	""" Sets the type of this class.

	Overrides Block.setType to account to account for sequences of
	values.
	"""
	if not hasattr(self, 'type'):
	    self.type = []
	if isinstance(value, (tuple, list)):
	    self.type.extend(value)
	elif value:
	    self.type.append(value)

    def getType(self):
	value = getattr(self, 'type', [])
	if isinstance(value, (basestring, )):
	    value = [value]
	return value

    def setEnumConstants(self, value):
	self.enumConstants = value

    def getEnumConstants(self):
	return self.enumConstants

    def addEnumConstant(self, value):
	print '### EC', value
	self.enumConstants.append(value)


class Method(PostDeclDocString, Block):
    """ Method -> type of block for Python methods.

    """
    isMethod = True

    def __init__(self, config):
	Block.__init__(self, config)
    	self.setParameters([])

    def iterPrologue(self):
	""" Returns the declaration for this method.

	"""
	for deco in self.getDecorators():
	    yield '@{0}'.format(deco)
	first = 'cls' if self.isStatic else 'self'
	params = ', '.join([first] + [str(p) for p in self.getParameters()])
	yield 'def {0}({1}):'.format(self.name, params)

    def getDecorators(self):
	decos = Block.getDecorators(self)[:]
	if self.isStatic and 'classmethod' not in decos:
	    decos.append('classmethod')
	return decos

    def getParameters(self):
	""" Returns the parameter sequence of this method.

	"""
	return self.parameters

    def setParameters(self, value):
	""" Sets the parameter sequence of this methods to the given value.

	"""
	self.parameters = value

    def addParameter(self, value):
	""" Adds the given value to this methods parameter sequence.

	"""
	self.parameters.append(value)


class Statement(Block):
    """ Statement -> type of block for Python statements.

    """
    ## keywords with a block indicator (:).  doesn't include "class"
    ## and "def" because we already have block types for those.
    ## doesn't include "elif", "lambda" and "with" because we don't
    ## generate those.
    blockKeywords = [
	'for',
	'if',
	'else',
	'try',
	'except',
	'finally',
	'while',
    ]


    def __init__(self, config, **kwds):
	Block.__init__(self, config)
	expr = Expression(self.getConfig(), format='{left}')
	self.setPrimaryExpression(expr)

    def iterPrologue(self):
	expr = self.getPrimaryExpression()
	expr = '' if expr.isEmpty() else ' {0}'.format(expr)
	yield '{0}{1}:'.format(self.getName(), expr)

    def getPrimaryExpression(self):
	return self.primaryExpression

    def setPrimaryExpression(self, value):
	self.primaryExpression = value

    def debugFormat(self):
	parts = (
	    color.white('<'),
	    color.magenta(self.className()),
	    color.white(' name:'), color.yellow(self.getName()),
	    color.white(' expr:'), color.yellow(self.getPrimaryExpression()),
	    color.white('>'),
	)
	return ''.join(parts)


class Expression(Block):
    """ Expression -> type of block for Python expressions.

    """
    keyNames = ('left', 'right', 'format', 'comment', 'type')

    def __init__(self, config, **kwds):
	Block.__init__(self, config)
	defaults = dict.fromkeys(self.keyNames, '')
	defaults.update(kwds)
	self.update(**defaults)

    def __nonzero__(self):
	""" x.__nonzero__() <==> x != 0

	"""
	return bool(self.format.strip())

    def dump(self, fd, indent=0):
	print >> fd, '{0}{1}'.format(self.getIndent()*indent, self)

    def __str__(self):
	""" x.__str__() <==> str(x)

	"""
	return self.format.format(**self.__dict__)

    def nestLeft(self, **kwds):
	""" Create and assign a new expression for the left of this one.

	"""
	self.left = left = self.new(self.getConfig(), **kwds)
	return left

    def nestRight(self, **kwds):
	""" Create and assign a new expression for the right of this one.

	"""
	self.right = right = self.new(self.getConfig(), **kwds)
	return right

    def addComment(self, comment):
	""" Places comments at the tail of this expression.

	"""
	start, stop, lines = comment
	cformat = '{comment}'
	if not self.format.count(cformat):
	    self.format = self.format + ' ' + self.getCommentPrefix() + cformat
	self.comment += ' '.join(lines)

    def debugFormat(self, title=''):
	""" Returns a formatted (maybe with color) string for this expression.

	"""
	parts = []
	add = lambda *x:parts.extend(x)
	add(color.white('<'))
	add(color.blue(title or self.className()))
	for name in self.keyNames:
	    attr = getattr(self, name, None)
	    ## types other than strings are not formatted; debugPrint
	    ## handles them directly.
	    if attr and isinstance(attr, (basestring, )):
		add(' ', color.white(name+':'), color.yellow(attr))
	add(color.white('>'))
	return ''.join(parts)

    def debugPrint(self, level=0, title=''):
	""" Prints the formatted string for this object to stderr.

	"""
	indent = self.getIndent()
	print >> sys.stderr, '{0}{1}'.format(indent*level, self.debugFormat(title))
	for name in ('left', 'right', 'type'):
	    obj = getattr(self, name, None)
	    printer = getattr(obj, 'debugPrint', lambda x, y:None)
	    printer(level+1, name.title())

    def isEmpty(self):
	return not any((self.left, self.right, self.type, self.comment))


class Comment(Expression):
    """ Comment -> type of expression that indicates it's a comment.

    """
    isComment = True


class BlockFactory(object):
    """ BlockFactory -> objects for building block instances.

    """
    ##
    # type mapping for lookups by name; implemented
    # as a class variable so that it can be manipulated
    # easily by client code.
    types = {
	'block'      : Block,
	'class'      : Class,
	'comment'    : Comment,
	'expression' : Expression,
	'method'     : Method,
	'module'     : Module,
	'statement'  : Statement,
    }

    def __init__(self, config):
	self.config = config

    def __call__(self, typeName, name=None, parent=None, **kwds):
	""" Creates a new block instance of the specified type (by name).

	"""
	try:
	    cls = self.types[typeName]
	except (KeyError, ):
	    raise TypeError('Unknown factory type: {0}'.format(typeName))
	block = cls(self.config, **kwds)
	block.setParent(parent)
	block.setName(name)
	return block
