#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""


"""
import itertools
import keyword
import StringIO

from java2python.lib import colortools as color
from java2python.lib import Formats as FS


class Block(object):
    """ Block -> basic block of Python code.

    """
    keywords = keyword.kwlist + ['None', 'str', ]

    def __init__(self, config):
	self.config = config
	self.children = []
	self.decorators = []
	self.modifiers = []
	self.name = None
	self.parent = None
	self.type = None
	self.variables = []

    @property
    def className(self):
	""" Returns the class name of this block.

	"""
	return self.__class__.__name__

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
	return iter(self.children)


    def iterEpilogue(self):
	"""
	"""
	yield None


    ##
    # default accessors

    @property
    def children(self):
	""" Returns sequence of children for this block.

	"""
	return self._children

    @children.setter
    def children(self, value):
	"""

	"""
	self._children = value

    def addChild(self, value):
	""" Adds a child to this block.

	"""
	self.children.append(value)

    def addComment(self, comment):
	""" Places comments at the end of this block.

	"""
	start, stop, lines = comment
	prefix = self.commentPrefix
	for line in lines:
	    comment = '{0}{1}'.format(prefix, line.rstrip().lstrip('\n'))
	    expr = Expression(config=self.config,
			      format='{comment}',
			      comment=comment, isComment=True)
	    expr.parent = self

    def addType(self, value):
	existing = self.type
	if existing is None:
	    value = [value]
	elif isinstance(existing, (basestring, )):
	    if value == existing:
		value = [existing]
	    else:
		value = [existing, value, ]
	elif isinstance(existing, (list, )):
	    if value not in existing:
		value = existing + [value]
	else:
	    raise Exception('Unhandled existing type')

	# this is gimpy.  fix it.
	tm = self.config.last('typeSubstitutionMap', {})
	typeMap = lambda t:tm.get(t, t)
	value = [typeMap(v) for v in value if v]
	self.type = value

    def addTypes(self, types):
	for typ in types:
	    self.addType(typ)

    def delType(self, value):
	try:
	    self._type.remove(value)
	except (ValueError, AttributeError, ):
	    pass

    @property
    def config(self):
	""" Returns the configuration object for this block.

	"""
	return self._config

    @config.setter
    def config(self, value):
	"""

	"""
	self._config = value

    @property
    def decorators(self):
	""" Returns the decorators of this block.

	"""
	return self._decorators

    @decorators.setter
    def decorators(self, value):
	"""

	"""
	self._decorators = value

    def addDecorator(self, value):
	""" Adds a decorator to this block.

	"""
	self.decorators.append(value)

    @property
    def modifiers(self):
	""" Returns the modifiers of this block.

	"""
	return self._modifiers

    @modifiers.setter
    def modifiers(self, value):
	self._modifiers = value

    def addModifier(self, value):
	""" Adds a modifier to this block.

	"""
	self.modifiers.append(value)

    @property
    def name(self):
	""" Returns the name of this block.

	"""
	return self._name

    @name.setter
    def name(self, value):
	""" Sets the name of this block.

	"""
	self._name = value

    @property
    def parent(self):
	""" Returns the parent of this block.

	"""
	return self._parent

    @parent.setter
    def parent(self, parent):
	""" Sets the parent of this block.

	"""
	self._parent = parent
	if hasattr(parent, 'addChild'):
	    parent.addChild(self)

    @property
    def type(self):
	""" Returns the type of this block.

	"""
	separator = '.'
	value = self._type
	if isinstance(value, (basestring, )):
	    return value
	elif isinstance(value, (tuple, list, )) and separator:
	    return separator.join(self._type)
	else:
	    return value

    @type.setter
    def type(self, value):
	""" Sets the type of this block.

	"""
	self._type = value

    @property
    def variables(self):
	""" Returns the variable sequence of this block.

	"""
	return self._variables

    @variables.setter
    def variables(self, value):
	""" Sets the variable sequence of this block to the given value.

	"""
	self._variables = value

    def addVariable(self, value):
	""" Adds the given value to the variable sequence of this block.

	"""
	self.variables.append(value)

    @property
    def indent(self):
	""" Returns the configured indent character(s) or the default.

	"""
	default = '    '
	return self.config.last('leadingIndent', default)

    @property
    def commentPrefix(self):
	""" Returns the configured comment prefix or the default.

	"""
	default = '# '
	return self.config.last('commentPrefix', default)

    @property
    def classes(self):
	for c in self.children:
	    if getattr(c, 'isClass', False):
		yield c

    @property
    def interfaces(self):
	for c in self.children:
	    if getattr(c, 'isInterface', False):
		yield c

    ##
    # output methods

    def dump(self, fd, level=0):
	""" dump(fd, [level]) -> prints this block to the given file-like object.

	The basic form of dumped lines looks like this:

	    # prologue
	        # child 1
                # child n
            # epilogue

	For modules, the prologue contains the docstring.  The
	epilogue contains the main script stanza (if any).

	For classes and methods, the prologue contains decorators and
	the declaration statement.  The docstring is contained within
	the children.  Enum constants are contained in the class
	epilogue.

	"""
	indent = level * self.indent
	isNotNone = lambda x:x is not None
	for line in itertools.ifilter(isNotNone, self.iterPrologue()):
	    print >> fd, '{0}{1}'.format(indent, line)
	for child in self.iterChildren():
	    child.dump(fd, level+1)
	for line in itertools.ifilter(isNotNone, self.iterEpilogue()):
	    print >> fd, '{0}{1}'.format(indent, line)

    def debugFormat(self):
	""" Returns a formatted (maybe with color) string for this block.

	"""
	parts = []
	add = lambda *x:parts.extend(x)
	add(color.white('<'), color.green(self.className))
	add(' ', color.white('name:'), color.cyan(self.name))
	add(' ', color.white('type:'), color.cyan(self.type or 'Unknown'))
	mods = self.modifiers
	if mods:
	    add(' ', color.white('mods:'), color.cyan(', '.join(mods)))
	add(color.white('>'))
	return ''.join(parts)

    def debugPrint(self, fd, level=0):
	""" Prints the formatted string for this object to stderr.

	"""
	indent = self.indent
	print >> fd, '{0}{1}'.format(indent*level, self.debugFormat())
	for child in [o for o in self.children if o]:
	    printer = getattr(child, 'debugPrint', lambda x, y:None)
	    printer(fd, level+1)


    ##
    # basic properties

    isClass = isComment = isEnum = isExpression = isMethod = isStatement = False

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

    ##
    # utilities

    def reparentChildren(self, target):
	""" Moves children of this block to target; adjusts types and parent.

	"""
	for child in self.children:
	    child.modifiers = self.modifiers
	    child.type = self.type
	    child.variables = self.variables
	    child.parent = target

    def update(self, **kwds):
	"""  Keyword-based attribute assignment; convenience for the grammar.

	"""
	for key, value in kwds.items():
	    setattr(self, key, value)

    def altName(self, value):
	if value in self.keywords:
	    value = '{0}_'.format(value)
	return value

    ## the first/last/handler methods on the config object are a mess.
    ## clean them up.

    def getHandler(self, value, prefix=None):
	if prefix is None:
	    prefix = self.className.lower()
	name = '{0}{1}'.format(prefix, value)
	return self.config.handler(name)

    def getHandlers(self, value, prefix=None):
	if prefix is None:
	    prefix = self.className.lower()
	name = '{0}{1}'.format(prefix, value)
	return self.config.handlers(name, all=True)

    def findVariable(self, name):
	if self.isMethod and name in [p['name'] for p in self.parameters]:
	    return name
	elif self.isMethod and name in self.variables:
	    return name
	elif self.isMethod and name in self.parent.variables:
	    if self.isStatic:
		return 'cls.{0}'.format(name)
	    else:
		return 'self.{0}'.format(name)
	else:
	    return name

    def packExpr(self, expr):
	parent = expr.parent
	children = getattr(parent, 'children', [])
	index = children.index(expr)
	if expr.isRightFormat and expr.hasRight:
	    children[index] = expr = self.toExpression(expr.right)
	elif expr.isLeftFormat and expr.hasLeft:
	    children[index] = expr = self.toExpression(expr.left)
	#nestedPackExpr(expr, self.toExpression(expr.right))
	#nestedPackExpr(expr, self.toExpression(expr.left))

    def toExpression(self, value):
	if getattr(value, 'isExpression', False):
	    return value
	return Expression(self.config, left=value, format=FS.l)


def nestedPackExpr(parent, child):
    if child.isRightFormat and child.hasRight:
	parent.right = child.right
    elif child.isLeftFormat and child.hasLeft:
	parent.left = child.left


class Module(Block):
    """ Module -> type of block for Python modules.

    """
    def __init__(self, config):
	Block.__init__(self, config)
	self.imports = []
	self.packages = []

    def __str__(self):
	""" Returns generated python source code for this Module.

	"""
	strfd = StringIO.StringIO()
	self.dump(strfd, -1)
	source = strfd.getvalue()
	for handler in self.getHandlers('OutputHandlers'):
	    source = handler(self, source)
	return source

    @property
    def imports(self):
	""" Returns sequence of imports for this module.

	"""
	return self._imports

    @imports.setter
    def imports(self, value):
	""" Sets the sequence of imports for this module.

	"""
	self._imports = value

    def addImport(self, value, static=False, star=False):
	""" Adds an import to this module.

	"""
	imp = (value, static, star)
	if imp not in self.imports:
	    self.imports.append(imp)

    @property
    def packages(self):
	""" Returns sequence of package statements for this module.

	"""
	return self._packages

    @packages.setter
    def packages(self, value):
	""" Sets the sequence of package statements for this module.

	"""
	self._packages = value

    def addPackage(self, value):
	""" Adds a package statement to this module.

	"""
	self.packages.append(value)

    def cleanup(self):
	""" Grammar helper called after parsing.

	TODO:  make this a configuration epilogue
	"""
	for handler in self.getHandlers('PostParseHandlers'):
	    handler(self)
	#self.addChild(Expression(config=self.config, format='\n'))

    def iterPrologue(self):
	""" iterPrologue -> yields module prologue lines by calling config handlers.

	"""
	for handler in self.getHandlers('PrologueHandlers'):
	    for line in handler(self):
		yield line

    def iterEpilogue(self):
	for handler in self.getHandlers('EpilogueHandlers'):
	    for line in handler(self):
		yield line


    def addBsrSource(self):
        from inspect import getsource
	from java2python.mods.includes import bsr
	if not getattr(self, 'bsrIncluded', False):
	    bsrExpr = Expression(self.config, format='{left}', left=getsource(bsr))
	    self.children.insert(0, bsrExpr)
	    self.bsrIncluded = True


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
	    children.append(Expression(self.config, format=doc, isDocString=True))
	children += self.children
	filtered = [c for c in children if not c.isComment]
	if not filtered:
	    children.append(Expression(self.config, format='pass'))
	return iter(children)


class Class(PostDeclDocString, Block):
    """ Class -> type of block for Python classes.

    """
    isClass = True
    isEnum = False
    isInterface = False

    def __init__(self, config):
	Block.__init__(self, config)
	self.enumConstants = []

    def iterChildren(self):
	""" Yields the children of this class with empty lines at
            various locations.

	"""
	last = Block(None)
	newline = Expression(self.config)
	for child in PostDeclDocString.iterChildren(self):
	    if child.isMethod and last.isExpression and not last.isDocString:
		yield newline
	    elif last.isMethod and child.isMethod:
		yield newline
	    elif last.isClass:
		yield newline
	    yield child
	    last = child

    def iterPrologue(self):
	""" Yields the declaration for this class.

	"""
	bases = ''
	handler = self.getHandler('BaseLookup')
	if handler:
	    bases = [b for b in handler(self) if b is not None]
	    bases = '({0})'.format(', '.join(bases)) if bases else ''
	yield 'class {0}{1}:'.format(self.name, bases)

    def iterEpilogue(self):
	if self.isEnum:
	    handler = self.getHandler('EpilogueHandler', prefix='enum')
	    print '### enum handler:', handler
	    for line in handler(self):
		yield line
	else:
	    pass

    @property
    def methods(self):
	for c in self.children:
	    if c.isMethod:
		yield c

    @property
    def type(self):
	value = self._type
	if isinstance(value, (basestring, )):
	    value = [value]
	return value

    @type.setter
    def type(self, value):
	""" Sets the type of this class.

	Overrides Block.type to account to account for sequences of
	values.
	"""
	if not hasattr(self, '_type'):
	    self._type = []
	typ = self._type
	if isinstance(value, (tuple, list)):
	    typ.extend([v for v in value if v not in typ])
	elif value and value not in typ:
	    typ.append(value)


    @property
    def enumConstants(self):
	return self._enumConstants

    @enumConstants.setter
    def enumConstants(self, value):
	self._enumConstants = value

    def addEnumConstant(self, value):
	self.enumConstants.append(value)

    def setVariation(self, isClass=False, isEnum=False, isInterface=False):
	self.isClass = isClass
	self.isEnum = isEnum
	self.isInterface = isInterface


class Method(PostDeclDocString, Block):
    """ Method -> type of block for Python methods.

    """
    isMethod = True
    requiresFirstParam = True

    def __init__(self, config):
	Block.__init__(self, config)
	self.parameters = []

    def iterPrologue(self):
	""" Yields the decorators (if any) and the declaration of this method.

	"""
	for deco in self.iterDecorators():
	    yield '@{0}'.format(deco)
	if self.requiresFirstParam:
	    first = ['cls' if self.isStatic else 'self']
	else:
	    first = []
	params = ', '.join(first + [p['name'] for p in self.parameters])
	yield 'def {0}({1}):'.format(self.name, params)

    def iterDecorators(self):
	"""

	"""
	def maybeHandlers():
	    for handler in self.getHandlers('PrologueHandlers'):
		for line in handler(self):
		    yield line

	def maybeClassMethodDeco():
	    if self.isStatic and 'classmethod' not in self.decorators:
		yield 'classmethod'
	return itertools.chain(self.decorators, maybeClassMethodDeco(), maybeHandlers())

    @property
    def parameters(self):
	""" Returns the parameter sequence of this method.

	"""
	return self._parameters

    @parameters.setter
    def parameters(self, value):
	""" Sets the parameter sequence of this methods to the given value.

	"""
	self._parameters = value

    def addParameter(self, name, type, dimensions=0, variadic=False):
	""" Adds the given value to this methods parameter sequence.

	"""
	tm = self.config.last('typeSubstitutionMap', {})
	type = tm.get(type, type)
        name = '*{0}'.format(name) if variadic else name
	param = dict(name=name, type=type, dimensions=dimensions)
	self.parameters.append(param)


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
    isStatement = True

    def __init__(self, config, **kwds):
	Block.__init__(self, config)
	self.primaryExpression = Expression(self.config, format='{left}')

    def iterPrologue(self):
	expr = self.primaryExpression
	expr = '' if expr.isEmpty else ' {0}'.format(expr)
	yield '{0}{1}:'.format(self.name, expr)

    @property
    def primaryExpression(self):
	return self._primaryExpression

    @primaryExpression.setter
    def primaryExpression(self, value):
	self._primaryExpression = value

    def debugFormat(self):
	parts = (
	    color.white('<'),
	    color.magenta(self.className),
	    color.white(' name:'), color.yellow(self.name),
	    color.white(' expr:'), color.yellow(self.primaryExpression),
	    color.white('>'),
	)
	return ''.join(parts)


class Expression(Block):
    """ Expression -> type of block for Python expressions.

    """
    isExpression = True
    isDocString = False
    keyNames = ('left', 'right', 'format', 'comment', 'type', 'rule', 'center')

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
	print >> fd, '{0}{1}'.format(self.indent*indent, self)

    def __str__(self):
	""" x.__str__() <==> str(x)

	"""
	values = dict((k, getattr(self, k)) for k in self.keyNames)
	try:
	    return self.format.format(**values)
	except (ValueError, ):
	    print '##', values
	    print '##', self.format
	    raise

    def nestLeft(self, **kwds):
	""" Create and assign a new expression for the left of this one.

	"""
	self.left = left = self.new(self.config, **kwds)
	left.parent = self
	return left

    def nestRight(self, **kwds):
	""" Create and assign a new expression for the right of this one.

	"""
	self.right = right = self.new(self.config, **kwds)
	right.parent = self
	return right

    def addComment(self, comment):
	""" Places comments at the tail of this expression.

	"""
	start, stop, lines = comment
	cformat = '{comment}'
	if not self.format.count(cformat):
	    self.format = self.format + ' ' + self.commentPrefix + cformat
	self.comment += ' '.join(lines)

    def debugFormat(self, title=''):
	""" Returns a formatted (maybe with color) string for this expression.

	"""
	parts = []
	add = lambda *x:parts.extend(x)
	add(color.white('<'))
	add(color.blue(title or self.className))
	for name in self.keyNames:
	    attr = getattr(self, name, None)
	    ## types other than strings are not formatted; debugPrint
	    ## handles them directly.
	    if attr and isinstance(attr, (basestring, )):
		add(' ', color.white(name+':'), color.yellow(attr))
	add(color.white('>'))
	return ''.join(parts)

    def debugPrint(self, fd, level=0, title=''):
	""" Prints the formatted string for this object to stderr.

	"""
	indent = self.indent
	print >> fd, '{0}{1}'.format(indent*level, self.debugFormat(title))
	for name in ('left', 'right', 'type'):
	    obj = getattr(self, name, None)
	    printer = getattr(obj, 'debugPrint', lambda x, y, z:None)
	    printer(fd, level+1, name.title())

    @property
    def isEmpty(self):
	return not any((self.left, self.right, self.type, self.comment))

    @property
    def hasLeft(self):
	return bool(self.left)

    @property
    def hasRight(self):
	return bool(self.right)

    @property
    def isLeftRightFormat(self):
	return self.format == FS.lr

    @property
    def isLeftFormat(self):
	return self.format == FS.l

    @property
    def isRightFormat(self):
	return (self.format == FS.r) or (self.format == FS.args)

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
	typ = kwds.pop('type', None)
	mods = kwds.pop('modifiers', None)
	block = cls(self.config, **kwds)
	block.parent = parent
	block.name = name
	if typ is not None:
	    block.addType(typ)
	if mods is not None:
	    block.modifiers.extend(mods)
	return block
