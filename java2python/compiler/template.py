#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" java2python.compiler.template -> Base classes for writing Python source. """
##
# This module defines base template types.  Each base class provides
# string representation methods (__str__, __repr__, dump, dumps) for
# serializing instances as source code.  The base types also provide
# many utility methods.
#
# The Factory class is used by the BaseTemplate class to provide
# runtime lookup of concrete classes; this was necessary to
# accommodate splitting the behavior of the blocks package into
# multiple modules.  So-called patterns are usually a sign of a bad
# design and/or language limitations, and this case is no exception.
#
from functools import partial
from itertools import ifilter
from StringIO import StringIO

from java2python.lang import tokens
from java2python.lib import FS
from java2python.lib.colortools import *



class Factory(object):
    """ Factory -> creates pre-configured callables for new block instances. """
    types = {}

    def __init__(self, config):
	self.config =  config

    def __getattr__(self, name):
	try:
	    return partial(self.types[name], self.config)
	except (KeyError, ):
	    raise AttributeError('Factory missing "{0}" type.'.format(name))


class FactoryTypeDetector(type):
    """ FactoryTypeDetector -> detects factory-creatable types as they are defined.

    """
    def __init__(cls, name, bases, namespace):
	try:
	    Factory.types[cls.factoryTypeName] = cls
	except (AttributeError, ):
	    pass


class BaseTemplate(object):
    """ BaseTemplate -> base class for formatting Python output.

    """
    __metaclass__ = FactoryTypeDetector
    isClass = isComment = isExpression = isMethod = isModule = False

    def __init__(self, config, name=None, type=None, parent=None):
	self.bases = []
	self.children = []
	self.config = config
	self.decorators = []
	self.factory = Factory(config)
	self.modifiers = []
	self.name = name
	self.parameters = []
	self.parent = parent
	self.type = type
	self.variables = []
	if parent:
	    parent.children.append(self)
	if self.isMethod:
	    self.parameters.append(self.makeParam('self', 'object'))

    def insertChild(self, child, index=-1):
	self.children.insert(index, child)
	child.parent = self

    def __repr__(self):
	""" Returns the debug string representation of this template. """
	name = white('name:') + cyan(self.name) if self.name else ''
	parts = [green(self.typeName), name]
	if self.type:
	    parts.append(white('type:') + cyan(self.type))
	if self.modifiers:
	    parts.append(white('modifiers:') + cyan(','.join(self.modifiers)))
	return ' '.join(parts)

    def __str__(self):
	""" Returns the Python source code representation of this template. """
	handlers = self.configHandlers('Output')
	return reduce(lambda v, func:func(self, v), handlers, self.dumps(-1))

    def altIdent(self, name):
	""" Returns an alternate identifier for the one given. """
	for klass in self.parents(lambda v:v.isClass):
	    if name in klass.variables:
		method = self.parents(lambda v:v.isMethod).next()
		if name in [p['name'] for p in method.parameters]:
		    return name
		return ('cls' if method.isStatic else 'self') + '.' + name
	return name

    def configHandler(self, part, suffix='Handler', default=None):
	""" Returns the config handler for this type of template. """
	name = '{0}{1}{2}'.format(self.typeName, part, suffix)
	return self.config.handler(name, default)

    def configHandlers(self, part, suffix='Handlers', default=None):
	""" Returns config handlers for this type of template """
	name = '{0}{1}{2}'.format(self.typeName, part, suffix)
	return self.config.handlers(name, default)

    def configTransformers(self, visitor):
	name = visitor.factoryTypeName
	name = '{0}Transformers'.format(name[0].lower() + name[1:])
	return name, self.config.handlers(name, ())

    def dump(self, fd, level=0):
	""" Writes the Python source code for this template to the given file. """
	indent, isNotNone = level * self.indent, lambda x:x is not None
	for line in ifilter(isNotNone, self.iterPrologue()):
	    line = '{0}{1}\n'.format(indent, line)
	    fd.write(line if line.strip() else '\n')
	for item in self.iterBody():
	    item.dump(fd, level+1)
	for line in ifilter(isNotNone, self.iterEpilogue()):
	    line = '{0}{1}\n'.format(indent, line)
	    fd.write(line if line.strip() else '\n')

    def dumps(self, level=0):
	""" Dumps this template to a string. """
	fd = StringIO()
	self.dump(fd, level)
	return fd.getvalue()

    def dumpRepr(self, fd, level=0):
	""" Writes a debug string for this template to the given file. """
	indent, default = self.indent, lambda x, y:None
	fd.write('{0}{1!r}\n'.format(indent*level, self))
	for child in ifilter(None, self.children):
	    getattr(child, 'dumpRepr', default)(fd, level+1)

    @property
    def indent(self):
	""" Returns the indent string for this item. """
	return self.config.last('indentPrefix', '    ')

    @property
    def isPublic(self):
	""" True if this item is static. """
	return 'public' in self.modifiers

    @property
    def isStatic(self):
	""" True if this item is static. """
	return 'static' in self.modifiers

    @property
    def isVoid(self):
	""" True if this item is void. """
	return 'void' == self.type

    def iterPrologue(self):
	""" Yields the items in the prologue of this template. """
	yield None

    def iterBody(self):
	""" Yields the items in the body of this template. """
        return iter(self.children)

    def iterEpilogue(self):
	""" Yields the items in the epilogue of this template. """
	yield None

    def makeParam(self, name, type):
	""" Creates a parameter as a mapping. """
	return dict(name=name, type=type)

    def parents(self, pred=lambda v:True):
	""" Yield each parent in the family tree. """
	while self:
	    if pred(self):
		yield self
	    self = self.parent

    @property
    def typeName(self):
	""" Returns the name of this template type. """
	return self.__class__.__name__.lower()


class BaseExpressionTemplate(BaseTemplate):
    """ BaseExpressionTemplate -> base class for formatting Python expressions.

    """
    isExpression = True

    def __init__(self, config, left='', right='', fs=FS.lr, parent=None, tail=''):
	super(BaseExpressionTemplate, self).__init__(config, parent=parent)
	self.left, self.right, self.fs, self.tail = left, right, fs, tail

    def __repr__(self):
	""" Returns the debug string representation of this template. """
	parts, parent, showfs = [blue(self.typeName)], self.parent, True
	if isinstance(self.left, (basestring, )) and self.left:
	    parts.append(white('left:') + yellow(self.left))
	    showfs = False
	if isinstance(self.right, (basestring, )) and self.right:
	    parts.append(white('right:') + yellow(self.right))
	    showfs = False
	if showfs:
	    parts.append(white('format:') + yellow(self.fs))
	if self.tail:
	    parts.append(white('tail:') + yellow(self.tail))
	return ' '.join(parts)

    def __str__(self):
	""" Returns the Python source code representation of this template. """
	return self.fs.format(left=self.left, right=self.right) + self.tail

    def dump(self, fd, level=0):
	""" Writes the Python source code for this template to the given file. """
	line = '{0}{1}\n'.format(self.indent*level, self)
	fd.write(line if line.strip() else '\n')

    def dumpRepr(self, fd, level=0):
	""" Writes a debug string for this template to the given file. """
	fd.write('{0}{1!r}\n'.format(self.indent*level, self))
	for obj in (self.left, self.right):
	    dumper = getattr(obj, 'dumpRepr', lambda x, y:None)
	    dumper(fd, level+1)

    @property
    def isComment(self):
	""" True if this expression is a comment. """
	try:
	    return self.left.startswith('#')
	except (AttributeError, ):
	    return False


class BaseCommentTemplate(BaseExpressionTemplate):
    """ BaseCommentTemplate -> base class for formatting Python comments. """

    def __repr__(self):
	""" Returns the debug string representation of this comment. """
	parts = [white(self.typeName+':'),
		 black(self.left) + black(self.right) + black(self.tail), ]
	return ' '.join(parts)



class BaseStatementTemplate(BaseTemplate):
    """ BaseStatementTemplate -> base class for formatting Python statements. """

    def __init__(self, config, keyword, fs=FS.lr, parent=None):
	super(BaseStatementTemplate, self).__init__(config, parent=parent)
	self.keyword = keyword
	self.expr = self.factory.expr(left=keyword, fs=fs)
	self.expr.parent = self

    def __repr__(self):
	""" Returns the debug string representation of this statement. """
	parts = [green(self.typeName), white('keyword:')+cyan(self.keyword)]
	return ' '.join(parts)
