#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" java2python.blocks -> AST visitors combined with python syntax templates.

"""
from functools import reduce
from itertools import *
from StringIO import StringIO

from java2python.block.util import *
from java2python.lib.colortools import *
from java2python.parser import tokens


#
# Base types
#


class PythonTemplate(object):
    """ PythonTemplate -> Base class for writing Python source code.

    """
    isClass = isMethod = False

    def __init__(self, config):
	self.config = config
	self.name = self.parent = self.type = None
	self.modifiers, self.children, self.variables = [], [], []

    def __repr__(self):
	""" Returns the debug string representation of this template. """
	parts = [green(self.typeName), ' ', white('name:'), cyan(self.name)]
	if self.type:
	    parts.extend([' ', white('type:'), cyan(self.type)])
	if self.modifiers:
	    mods = cyan(','.join(self.modifiers))
	    parts.extend([' ', white('modifiers:'), mods])
	return ''.join([black('[')] + parts + [black(']')])

    def __str__(self):
	""" Returns the Python source code representation of this template. """
	fd = StringIO()
	self.dump(fd, -1)
	handlers = self.configHandlers('OutputHandlers')
	return reduce(lambda v, func:func(self, v), handlers, fd.getvalue())

    @classmethod
    def build(cls, parent, name=None, type=None):
	""" Alternate constructor for this template type. """
	obj = cls(parent.config)
	obj.name, obj.parent, obj.type = name, parent, type
	parent.children.append(obj)
	return obj

    def configHandler(self, part, default=None):
	""" Returns the config handler for this type of template. """
	name = '{0}{1}'.format(self.typeName, part)
	return self.config.handler(name, default)

    def configHandlers(self, part, default=None):
	""" Returns config handlers for this type of template """
	name = '{0}{1}'.format(self.typeName, part)
	return self.config.handlers(name, default)

    def dump(self, fd, level=0):
	""" Writes the Python source code for this template to the given file. """
	indent, isNotNone = level * self.indent, lambda x:x is not None
	for line in ifilter(isNotNone, self.iterPrologue()):
	    fd.write('{0}{1}\n'.format(indent, line))
	for item in self.iterBody():
	    item.dump(fd, level+1)
	for line in ifilter(isNotNone, self.iterEpilogue()):
	    fd.write('{0}{1}\n'.format(indent, line))

    def dumpRepr(self, fd, level=0):
	""" Writes a debug string for this template to the given file. """
	indent, default = self.indent, lambda x, y:None
	fd.write('{0}{1!r}\n'.format(indent*level, self))
	for child in ifilter(None, self.children):
	    getattr(child, 'dumpRepr', default)(fd, level+1)

    @property
    def indent(self):
	""" Returns the indent string for this item. """
	return self.config.last('leadingIndent', '    ')

    def iterPrologue(self):
	""" Yields the items in the prologue of this template. """
	yield None

    def iterBody(self):
	""" Yields the items in the body of this template. """
	## TODO:  account for docstrings
	if self.children:
	    return iter(self.children)
	return iter([Expression(self.config, left='pass')])

    def iterEpilogue(self):
	""" Yields the items in the epilogue of this template. """
	yield None

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

    @property
    def typeName(self):
	""" Returns the name of this template type. """
	return self.__class__.__name__.lower()


class Visitor(object):
    """ Visitor -> Base class for AST visitors.

    """
    def walk(self, tree):
	""" Depth-first visiting of the given AST. """
	visitor = self.accept(tree)
	if visitor:
	    map(visitor.walk, tree.children)

    def accept(self, node):
	""" Accept a node, possibly creating a child visitor. """
	title = tokens.title(tokens.map.get(node.token.type))
	return getattr(self, 'accept{0}'.format(title), lambda n:self)(node)

    def acceptClass(self, node):
	""" Creates a new class.  Called on Module and Class templates. """
	name = nodeFirstChildOfType(node, tokens.IDENT).text
	self.variables.append(name)
	return Class.build(self, name=name)

    def acceptVarDeclaration(self, node):
	""" Creates a new expression for a variable declaration. """
	mods = nodeChildrenOfType(node, tokens.MODIFIER_LIST)
	decl = nodeFirstChildOfType(node, tokens.VAR_DECLARATOR_LIST)
	for vard in nodeChildrenOfType(decl, tokens.VAR_DECLARATOR):
	    ident = nodeFirstChildOfType(vard, tokens.IDENT)
    	    expr = nodeFirstChildOfType(vard, tokens.EXPR)
	    child = Expression.build(self, left=ident.text)
	    assgn = child.pushRight(' = ')
	    if expr:
		assgn.walk(expr)
	    else:
		typ = nodeFirstChildOfType(node, tokens.TYPE)
		typ = typ.children[0].text
		val = assgn.pushRight()
		val.left = '{0}()'.format(typ) # wrong
	return self


class SharedIteratorsTemplate(object):
    def iterPrologue(self):
	""" Yields the items in the prologue of this template. """
	for handler in self.configHandlers('PrologueHandlers'):
	    for line in handler(self):
		yield line

    def iterEpilogue(self):
	""" Yields the items in the epilogue of this template. """
	for handler in self.configHandlers('EpilogueHandlers'):
	    for line in handler(self):
		yield line

#
# Module types
#


class ModuleTemplate(SharedIteratorsTemplate, PythonTemplate):
    """ ModuleTemplate -> represents a Python module. """


class ModuleVisitor(Visitor):
    """ ModuleVisitor -> accepts AST branches for module-level objects. """


#
# Class types
#


class ClassTemplate(SharedIteratorsTemplate, PythonTemplate):
    """ ClassTemplate -> represents a Python class.

    """
    isClass = True

    def __init__(self, config):
	PythonTemplate.__init__(self, config)
	self.bases = []

    def iterPrologue(self):
	""" Yields the items in the prologue of this template. """
	handler = self.configHandler('BaseHandler', lambda b:b)
	bases = [b for b in handler(self) if b is not None]
        bases = '({0})'.format(', '.join(bases)) if bases else ''
	yield 'class {0}{1}:'.format(self.name, bases)


class ClassVisitor(Visitor):
    """ ClassVisitor -> accepts AST branches for class-level objects.

    """
    def acceptExtendsClause(self, node):
	""" Accept and process an extends clause. """
	names = (n.text for n in nodeFindChildrenOfType(node, tokens.IDENT))
	self.bases.append('.'.join(names))

    def acceptVoidMethodDecl(self, node):
	""" Accept and process a void method declaration. """
	ident = nodeFirstChildOfType(node, tokens.IDENT)
	method = Method.build(self, name=ident.text, type='void')
	return method

    def acceptFunctionMethodDecl(self, node):
	""" Accept and process a typed method declaration. """
	ident = nodeFirstChildOfType(node, tokens.IDENT)
	type = nodeFirstChildOfType(node, tokens.TYPE).children[0].text
	method = Method.build(self, name=ident.text, type=type)
	return method


#
# Method types
#


class MethodTemplate(PythonTemplate):
    """ MethodTemplte -> represents a Python method.

    """
    isMethod = requiresFirstParam = True

    def __init__(self, config):
	PythonTemplate.__init__(self, config)
	self.decorators, self.parameters = [], []

    def iterDecorators(self):
	""" Yields decorators for this method. """
	def iterLines():
	    for handler in self.configHandlers('PrologueHandlers'):
		for line in handler(self):
		    yield line
	def iterOtherDecos():
	    if self.isStatic and 'classmethod' not in self.decorators:
		yield 'classmethod'
	return chain(self.decorators, iterOtherDecos(), iterLines())

    def iterPrologue(self):
	""" Yields items in this method declaration, maybe with decorators. """
	for deco in self.iterDecorators():
	    yield '@{0}'.format(deco)
	if self.requiresFirstParam:
	    first = ['cls' if self.isStatic else 'self']
	else:
	    first = []
	params = ', '.join(first + [p['name'] for p in self.parameters])
	yield 'def {0}({1}):'.format(self.name, params)


class MethodContentVisitor(Visitor):
    """ MethodContentVisitor -> accepts AST branches for blocks within methods.

    """
    def acceptAssert(self, node):
	""" Accept and process an assert statement. """
	assertStat = Statement.build(self, 'assert', fs=FS.lsr)
	assertStat.expr.walk(nodeFirstChild(node))

    def acceptThrow(self, node):
	""" Accept and process a throw statement. """
	throw = Statement.build(self, 'raise', fs=FS.lsr)
	throw.expr.walk(node.children[0])

    def acceptTry(self, node):
	""" Accept and process a try/catch block. """
	children = node.children
	tryNode = children[0]
	if len(children) == 3:
	    catchClausesNode, finNode = children[1:3]
	elif len(children) == 2:
	    catchClausesNode = finNode = None
	    if children[1].type == tokens.CATCH_CLAUSE_LIST:
		catchClausesNode = children[1]
	    else:
		finNode = children[1]
        tryStat = Statement.build(self, 'try', fs=FS.lc)
	tryStat.walk(tryNode)
	if catchClausesNode:
	    for catchNode in catchClausesNode.children:
		exStat = ExceptStatement.build(self, 'except', fs=FS.lsrc)
		exStat.walk(catchNode)
	if finNode:
	    finStat = Statement.build(self, 'finally', fs=FS.lc)
	    finStat.walk(finNode)

    def acceptExpr(self, node):
	""" Creates a new expression. """
	if nodeParentType(node) == tokens.BLOCK_SCOPE: # wrong
	    return Expression.build(self)

    def acceptReturn(self, node):
	""" Creates a new return expression. """
	if nodeParentType(node) == tokens.BLOCK_SCOPE: # wrong
	    expr = Expression.build(self, left='return')
	    if node.children:
		expr.fs, expr.right = FS.lsr, Expression.build(expr)
		expr.right.walk(node)


class MethodVisitor(MethodContentVisitor):
    """ MethodVisitor -> accepts AST branches for method-level objects.

    """
    def acceptModifierList(self, node):
	""" Accept and process method modifiers. """
	if nodeParentType(node) in tokens.methodTypes:
	    self.modifiers.extend(n.text for n in nodeChildren(node))
	return self

    def acceptFormalParamStdDecl(self, node):
	""" Accept and process a single parameter declaration. """
	ident = nodeFirstChildOfType(node, tokens.IDENT)
	self.parameters.append({'name':ident.text})
	return self

    def acceptFormalParamVarargDecl(self, node):
	""" Accept and process a var arg declaration. """
	ident = nodeFirstChildOfType(node, tokens.IDENT)
	self.parameters.append({'name':'*{0}'.format(ident.text)})
	return self


#
# Expression types
#


class ExpressionTemplate(PythonTemplate):
    """ ExpressionTemplate -> represents a Python expression.

    """
    def __init__(self, config, left='', right='', fs=FS.lr):
	PythonTemplate.__init__(self, config)
	self.left, self.right, self.fs = left, right, fs

    def __repr__(self):
	""" Returns the debug string representation of this template. """
	parts = [blue(self.typeName)]
	if isinstance(self.left, (basestring, )):
	    parts.extend([' ', yellow(self.left)])
	if isinstance(self.right, (basestring, )):
	    parts.append(yellow(self.right))
	return ''.join([black('[')] + parts + [black(']')])

    def __str__(self):
	""" Returns the Python source code representation of this template. """
	return self.fs.format(left=self.left, right=self.right)

    @property
    def typeName(self):
	""" Returns the name of this template type. """
	parent = self.parent
	name = self.__class__.__name__.lower()
	if isinstance(parent, (Expression, )):
	    if self is parent.left:
		name = 'left'
	    if self is parent.right:
		name = 'right'
	return name

    @classmethod
    def build(cls, parent, left='', right='', fs=FS.lr):
	""" Alternate constructor for this template type. """
	obj = cls(parent.config, left=left, right=right, fs=fs)
	obj.parent = parent
	parent.children.append(obj)
	return obj

    def dump(self, fd, level=0):
	""" Writes the Python source code for this template to the given file. """
	fd.write('{0}{1}\n'.format(self.indent*level, self))

    def dumpRepr(self, fd, level=0):
	""" Writes a debug string for this template to the given file. """
	fd.write('{0}{1!r}\n'.format(self.indent*level, self))
	for obj in (self.left, self.right):
	    dumper = getattr(obj, 'dumpRepr', lambda x, y:None)
	    dumper(fd, level+1)


class ExpressionVisitor(Visitor):
    """ ClassVisitor -> accepts AST branches for expression objects.

    """
    def textExpression(self, node):
	""" Assigns node text to the left side of this expression. """
	self.left = node.text

    acceptIdent = textExpression
    acceptCharacterLiteral = textExpression
    acceptStringLiteral = textExpression
    acceptFloatingPointLiteral = textExpression
    acceptDecimalLiteral = textExpression
    acceptHexLiteral = textExpression
    acceptOctalLiteral = textExpression
    acceptTrue = textExpression
    acceptFalse = textExpression
    acceptNull = textExpression

    def equalityExpression(self, node):
	""" Accept and processes an equality expression. """
	self.fs = FS.l + ' ' + node.text + ' ' + FS.r
	self.left, self.right = Expression.build(self), Expression(self.config)
	self.walkThisWay(nodeChildren(node), (self.left, self.right))

    acceptEqual = equalityExpression
    acceptGreaterOrEqual = equalityExpression
    acceptGreaterThan = equalityExpression
    acceptLessOrEqual = equalityExpression
    acceptLessThan = equalityExpression
    acceptNotEqual = equalityExpression

    def assignExpression(self, node):
	""" Accept and processes an assignment expression (Python statement). """
	self.fs = FS.l + ' ' + node.text + ' ' + FS.r
	self.left, self.right = Expression.build(self), Expression(self.config)
	self.walkThisWay(nodeChildren(node), (self.left, self.right))

    acceptAssign = assignExpression
    acceptPlusAssign = assignExpression
    acceptMinusAssign = assignExpression
    acceptStarAssign = assignExpression
    acceptDivAssign = assignExpression
    acceptAndAssign = assignExpression
    acceptOrAssign = assignExpression
    acceptXorAssign = assignExpression
    acceptModAssign = assignExpression
    acceptShiftLeftAssign = assignExpression
    acceptShiftRightAssign = assignExpression

    def walkThisWay(self, nodes, exprs):
	for node, expr in izip(nodes, exprs):
	    expr.walk(node)

    def acceptExpr(self, node):
	""" Create a new expression within this one. """
	return self.pushRight()

    def acceptClassConstructorCall(self, node):
	""" Accept and process a class constructor call. """
	self.acceptMethodCall(node) # probably wrong

    def acceptMethodCall(self, node):
	""" Accept and process a method call. """
	self.fs = FS.l + '(' + FS.r + ')'
	self.left, self.right = Expression.build(self), Expression.build(self)
	self.left.walk(nodeFirstChild(node))
	self.right.walk(nodeFirstChildOfType(node, tokens.ARGUMENT_LIST))

    def acceptDot(self, node):
	""" Accept and process a dotted expression. """
	self.fs = FS.l + '.' + FS.r
	self.left, self.right = Expression.build(self), Expression.build(self)
	self.walkThisWay(nodeChildren(node), (self.left, self.right))

    def acceptQuestion(self, node):
	""" Accept and process a terinary expression. """
	self.fs = FS.l + ' if ' + FS.r
	self.left = Expression.build(self)
	self.right = Expression.build(self, fs=FS.l + ' else ' + FS.r)
        self.right.left = Expression.build(self.right)
	self.right.right = Expression.build(self.right)
	self.walkThisWay(nodeChildren(node), (self.right.left, self.left, self.right.right))

    def pushRight(self, value=''):
	""" Creates a new right expression, sets it, and returns it. """
	self.right = Expression.build(self, left=value)
	return self.right


#
# Statement types
#


class StatementTemplate(PythonTemplate):
    @classmethod
    def build(cls, parent, keyword, fs=FS.lr):
	""" Alternate constructor for this template type. """
	obj = cls(parent.config)
	parent.children.append(obj)
	obj.keyword = keyword
	obj.expr = Expression(obj.config, left=keyword, fs=fs)
	return obj

    def __repr__(self):
	""" Returns the debug string representation of this template. """
	parts = [green('statement'), ' ', white('keyword:'), cyan(self.keyword)]
	return ''.join([black('[')] + parts + [black(']')])

    def iterPrologue(self):
	""" Yields the keyword (and clause, if any) for this statement . """
	yield self.expr

    def iterBody(self):
	""" Yields the items in the body of this template. """
	return iter(self.children)


class StatementVisitor(MethodContentVisitor):
    """ StatementVisitor -> accepts AST branches for statement objects. """


class ExceptStatementVisitor(MethodContentVisitor):
    """ ExceptStatementVisitor -> accepts AST branches for 'except' statements.

    """
    def acceptCatch(self, node):
	""" Accept and process a catch statement. """
	decl = nodeFirstChildOfType(node, tokens.FORMAL_PARAM_STD_DECL)
	dtype = nodeFirstChildOfType(decl, tokens.TYPE)
	tnames = nodeFindChildrenOfType(dtype, tokens.IDENT)
	cname = '.'.join(n.text for n in tnames)
	cname = self.config.combined('exceptionSubMap').get(cname, cname)
	cvar = nodeFirstChildOfType(decl, tokens.IDENT)
	block = nodeFirstChildOfType(node, tokens.BLOCK_SCOPE)
	self.expr.fs = FS.lsrc
	self.expr.right = Expression(self.config, fs=FS.l+' as '+FS.r, left=cname, right=cvar)
	self.walk(block)


#
# Concrete client types
#

class Module(ModuleTemplate, ModuleVisitor):
    """ Module -> represents a Python module. """


class Class(ClassTemplate, ClassVisitor):
    """ Class -> represents a Python class. """


class Method(MethodTemplate, MethodVisitor):
    """ Method -> represents a Python method. """


class Expression(ExpressionTemplate, ExpressionVisitor):
    """ Expression -> represents a Python expression. """


class Statement(StatementTemplate, StatementVisitor):
    """ Statement -> represents a Python statement. """


class ExceptStatement(StatementTemplate, ExceptStatementVisitor):
    """ ExceptStatement -> represents a Python 'except' statement. """
