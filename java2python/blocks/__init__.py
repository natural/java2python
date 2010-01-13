#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import chain
from keyword import kwlist
from sys import stderr

from java2python.lib import Formats
from java2python.lib.colortools import red, yellow, green, cyan, white, magenta, blue


class Block:
    """ Block -> basic block of Python code.

    """
    keywords = kwlist + ['None', 'str', ]

    def __init__(self, config):
	self.setConfig(config)
	self.setChildren([])
	self.setDecorators([])
	self.setModifiers([])
	self.setName(None)
	self.setParent(None)
	self.setType(None)
	self.setVariables([])

    def __str__(self):
	""" x.__str__() <==> str(x)

	"""
	preamble = self.getPreamble()
	indent = self.indent()
	decs = self.getDeclaration()
	#decs = ['%s%s' % (indent*self.getDepth(), d) for d in decs]
	docs = self.getDocString()
	docs = ['%s%s' % (indent*(1+self.getDepth()), s) for s in docs]
        body = ['%s%s' % (indent*o.getDepth(), o) for o in self.getChildren()]
	text = u'\n'.join(preamble + decs + docs + body)
	return self.applyOutputHandlers(text)

    def setConfig(self, config):
	""" Sets the configuration object for this block.

	"""
	self.config = config

    def getDeclaration(self):
	""" Returns the declaration for this block.

	"""
	return []

    def getPreamble(self):
	""" Returns a sequence of preamble lines for this block.

	"""
	name = '%sPreamble' % self.blockTypeName()
	preambles = self.config.handlers(name, all=True)
	return list(chain(*[p(self) for p in preambles]))

    def getDocString(self):
	""" Returns a sequence of docstring lines for this block.

	"""
	name = '%sDocString' % self.blockTypeName()
	docstrings = self.config.handlers(name, all=True)
	return list(chain(*[p(self) for p in docstrings]))

    def applyOutputHandlers(self, text):
	name = '%sOutputHandlers' % self.blockTypeName()
	for handler in self.config.handlers(name, all=True):
	    text = handler(self, text)
	return text

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
	config = self.config
	lformat = Formats.left
	for line in lines:
	    left = self.commentPrefix() + '%s' % line.rstrip().lstrip('\n')
	    comment = Comment(config=config, format=lformat, left=left)
	    comment.setParent(self)

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
	self.name = self.altName(value)

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

    def getDepth(self):
	""" Returns the depth of this block based on it's parents.

	"""
	depth = 0
	if self.parentIsModule():
	    return depth
	while self:
	    if self.parent and not self.parentIsModule():
		self = self.parent
		depth += 1
	    else:
		return depth
	return depth

    ##
    # utilities

    def debugFormat(self):
	""" Returns a formatted (maybe with color) string for this block.

	"""
	parts = []
	add = lambda *x:parts.extend(x)
	add(white('<'))
	add(green(self.blockTypeName().title()))
	add(' ', white('name:'), cyan(self.getName()))
	add(' ', white('type:'), cyan(self.getType() or 'Unknown'))
	mods = self.getModifiers()
	if mods:
	    add(' ', white('mods:'), cyan(', '.join(self.getModifiers())))
	add(white('>'))
	return ''.join(parts)

    def debugPrint(self, level=0):
	""" Prints the formatted string for this object to stderr.

	"""
	indent = self.indent()
	print >> stderr, '%s%s' % (indent*level, self.debugFormat())
	for child in [o for o in self.getChildren() if o]:
	    printer = getattr(child, 'debugPrint', lambda v:None)
	    printer(level+1)

    def isComment(self):
	""" Returns True if this block is a comment.

	"""
	return isinstance(self, (Comment, ))

    def indent(self, default='    '):
	""" Returns the configured indent character(s) or the default.

	"""
	return self.config.last('leadingIndent', default)

    def commentPrefix(self, default='# '):
	""" Returns the configured comment prefix or the default.

	"""
	return self.config.last('commentPrefix', default)

    def isPublic(self):
	""" True if this block has a 'public' modifier.

	"""
	return 'public' in self.modifiers

    def isStatic(self):
	""" True if this block has a 'static' modifier.

	"""
	return 'static' in self.modifiers

    def isVoid(self):
	""" True if the type of this block is 'void'.

	"""
	return 'void' == self.type

    @classmethod
    def new(cls, config, **kwds):
	""" Creates another block of the same type as this one.

	"""
	return cls(config, **kwds)

    def parentIsModule(self):
	""" True if the parent of this block is a Module.

	"""
	return isinstance(self.parent, (Module, ))

    def reparentChildren(self, target):
	""" Moves children of this block to target; adjusts types and parent.

	"""
	for child in self.getChildren():
	    child.modifiers = self.modifiers
	    child.type = self.type
	    child.variables = self.variables
	    child.setParent(target)

    def getAtLeastOneChild(self):
	""" Children accesor that ensures there is at least one child.

	"""
	children = self.children[:]
	filtered = [c for c in children if not c.isComment()]
	if not filtered:
	    comment = Expression(self.config, format=Formats.left, left='pass')
	    comment.setParent(self, autoAdd=False)
	    children.append(comment)
	return children + [Expression(self.config, format=''), ]

    def update(self, **kwds):
	"""  Keyword-based attribute assignment; convenience for the grammar.

	"""
	for key, value in kwds.items():
	    setattr(self, key, value)

    def altName(self, value):
	if value in self.keywords:
	    value = '%s_' % (value, )
	return value

    def blockTypeName(self):
	return self.__class__.__name__.lower()

class Module(Block):
    """ Module -> type of block for Python modules.

    """
    def __init__(self, config):
	Block.__init__(self, config)
    	self.setPackages([])
    	self.setImports([])

    def getImports(self):
	""" Returns sequence of imports for this module.

	"""
	return self.imports

    def setImports(self, value):
	""" Sets the sequence of imports for this module.

	"""
	self.imports = value

    def addImport(self, value, isStatic=False, dotStar=False):
	""" Adds an import to this module.

	"""
	self.imports.append((value, isStatic, dotStar))

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
	self.addChild(Expression(config=self.config, format='\n'))


class Class(Block):
    """ Class -> type of block for Python classes.

    """
    def __init__(self, config):
	Block.__init__(self, config)
	self.getChildren = self.getAtLeastOneChild

    def getDeclaration(self):
	""" Returns the declaration for this class.

	"""
	types = ', '.join(self.type or ['object']) # make config
	types = '(%s)' % types if types else ''
	return ['class %s%s:' % (self.name, types), ]

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


class Method(Block):
    """ Method -> type of block for Python methods.

    """
    def __init__(self, config):
	Block.__init__(self, config)
    	self.setParameters([])
	self.getChildren = self.getAtLeastOneChild

    def getDeclaration(self):
	""" Returns the declaration for this method.

	"""
	first = 'cls' if self.isStatic() else 'self'
	params = ', '.join([first] + [str(p) for p in self.getParameters()])
	#lines = ['@'+deco for deco in self.getDecorators()]
	# TODO:  fix decorator / declaration formating
	lines = []
	lines.append('def %s(%s):' % (self.name, params))
	#for line in lines:
	#    print '###LINE: %s ###' % (line, )
	return lines

    def getDecorators(self):
	return ['classmethod', ]

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
	self.setPrimaryExpression(Expression(self.config, format='{left}'))

    def getDeclaration(self):
	items = []
	expr = self.getPrimaryExpression()
	if not any((expr.left, expr.right, expr.comment, expr.type)):
	    expr = ''
	else:
	    expr = ' %s' % (expr, )
	items.append('%s%s:' % (self.getName(), expr))
	return items

    def getPrimaryExpression(self):
	return self.primaryExpression

    def setPrimaryExpression(self, value):
	self.primaryExpression = value

    def debugFormat(self):
	parts = []
	add = lambda *x:parts.extend(x)
	add(white('<'))
	add(magenta('%s' % self.blockTypeName().title()))
	add(white(' name:'), yellow(self.getName()))
	add(white(' expr:'), yellow(self.getPrimaryExpression()))
	add(white('>'))
	return ''.join(parts)


class Expression(Block):
    """ Expression -> type of block for Python expressions.

    """
    def __init__(self, config, **kwds):
	Block.__init__(self, config)
	defaults = dict(left='', right='', format='', comment='')
	defaults.update(kwds)
	self.update(**defaults)

    def __nonzero__(self):
	""" x.__nonzero__() <==> x != 0

	"""
	return bool(self.format.strip())

    def __str__(self):
	""" x.__str__() <==> str(x)

	"""
	return self.format.format(**self.__dict__)

    def nestLeft(self, **kwds):
	""" Create and assign a new expression for the left of this one.

	"""
	self.left = left = self.new(self.config, **kwds)
	return left

    def nestRight(self, **kwds):
	""" Create and assign a new expression for the right of this one.

	"""
	self.right = right = self.new(self.config, **kwds)
	return right

    def addComment(self, comment):
	""" Places comments at the tail of this expression.

	"""
	start, stop, lines = comment
	cformat = Formats.comment
	if not self.format.count(cformat):
	    self.format = self.format + ' ' + self.commentPrefix() + cformat
	self.comment += ' '.join(lines)

    def debugFormat(self, title=''):
	""" Returns a formatted (maybe with color) string for this expression.

	"""
	parts = []
	add = lambda *x:parts.extend(x)
	add(white('<'))
	add(blue('%s' % (title or self.blockTypeName().title())))
	for name in ('format', 'left', 'right', 'type'):
	    attr = getattr(self, name, None)
	    ## types other than strings are not formatted; debugPrint
	    ## handles them directly.
	    if attr and isinstance(attr, (basestring, )):
		add(' ', white(name+':'), yellow(attr))
	add(white('>'))
	return ''.join(parts)

    def debugPrint(self, level=0, title=''):
	""" Prints the formatted string for this object to stderr.

	"""
	indent = self.indent()
	print >> stderr, '%s%s' % (indent*level, self.debugFormat(title))
	for name in ('left', 'right', 'type'):
	    obj = getattr(self, name, None)
	    printer = getattr(obj, 'debugPrint', lambda x, y:None)
	    printer(level+1, name.title())

    @property
    def leafless(self):
	return not any((self.left, self.right, self.type, self.comment))

class Comment(Expression):
    """ Comment -> type of expression that indicates it's a comment.

    """


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
	    raise TypeError('Unknown factory type: %s' % (typeName, ))
	block = cls(self.config, **kwds)
	block.setParent(parent)
	block.setName(name)
	return block
