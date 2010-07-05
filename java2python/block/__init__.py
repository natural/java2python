#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" java2python.blocks -> AST visitors combined with python syntax templates.

"""
from functools import reduce
from itertools import chain

from java2python.block.template import BaseExpressionTemplate, BaseTemplate, CommonIterMixin
from java2python.block.visitor import BaseVisitor
from java2python.lib import FS
from java2python.lib.colortools import *
from java2python.parser import tokens


class ModuleTemplate(CommonIterMixin, BaseTemplate):
    """ ModuleTemplate -> represents a Python module. """


class ModuleVisitor(BaseVisitor):
    """ ModuleVisitor -> accepts AST branches for module-level objects. """


class ClassTemplate(CommonIterMixin, BaseTemplate):
    """ ClassTemplate -> represents a Python class. """
    isClass = True

    def __init__(self, config, name=None, type=None, parent=None):
	super(ClassTemplate, self).__init__(config, name=name, type=type, parent=parent)
	self.bases = []

    def iterPrologue(self):
	""" Yields the items in the prologue of this template. """
	handler = self.configHandler('BaseHandler', lambda b:b)
	bases = [b for b in handler(self) if b is not None]
        bases = '({0})'.format(', '.join(bases)) if bases else ''
	yield 'class {0}{1}:'.format(self.name, bases)

    def iterBody(self):
	""" Yields the items in the body of this template. """
	def iterDocString():
	    for handler in self.configHandlers('DocStringHandlers'):
		for line in handler(self):
		    yield self.factory.expr(left=line)
	def intersperseLines(lines):
	    get = lambda o, n:getattr(o, n, None)
	    blank, prev = self.factory.expr(), None
	    for item in lines:
		if type(item) != type(prev) and prev:
		    yield blank
		elif get(item, 'isMethod') and get(prev, 'isMethod'):
		    yield blank
		elif get(prev, 'isClass'):
		    yield blank
		yield item
		prev = item
	body = list(super(ClassTemplate, self).iterBody())
	docs = list(iterDocString())
	more = [self.factory.expr(left='pass')] if not (body or docs) else []
	return chain(docs, iter(body) if more else intersperseLines(body), more)


class ClassVisitor(BaseVisitor):
    """ ClassVisitor -> accepts AST branches for class-level objects. """

    def acceptVarDeclaration(self, node):
	""" Creates a new expression for a variable declaration. """
	mods = node.childrenOfType(tokens.MODIFIER_LIST)
	decl = node.firstChildOfType(tokens.VAR_DECLARATOR_LIST)
	for vard in decl.childrenOfType(tokens.VAR_DECLARATOR):
	    ident = vard.firstChildOfType(tokens.IDENT)
    	    expr = vard.firstChildOfType(tokens.EXPR)
	    child = self.factory.expr(left=ident.text, parent=self)
	    assgn = child.pushRight(' = ')
	    if expr:
		assgn.walk(expr)
	    else:
		typ = node.firstChildOfType(tokens.TYPE)
		typ = typ.children[0].text
		val = assgn.pushRight()
		val.left = '{0}()'.format(typ) # wrong
	return self

    def acceptConstructorDecl(self, node):
	""" Accept and process a constructor declaration. """
	return self.factory.method(name='__init__', type=self.name, parent=self)

    def acceptExtendsClause(self, node):
	""" Accept and process an extends clause. """
	names = (n.text for n in node.findChildrenOfType(tokens.IDENT))
	self.bases.append('.'.join(names))

    def acceptFunctionMethodDecl(self, node):
	""" Accept and process a typed method declaration. """
	ident = node.firstChildOfType(tokens.IDENT)
	type = node.firstChildOfType(tokens.TYPE).children[0].text
	return self.factory.method(name=ident.text, type=type, parent=self)

    def acceptVoidMethodDecl(self, node):
	""" Accept and process a void method declaration. """
	ident = node.firstChildOfType(tokens.IDENT)
	return self.factory.method(name=ident.text, type='void', parent=self)


class MethodTemplate(BaseTemplate):
    """ MethodTemplte -> represents a Python method. """
    isMethod = requiresFirstParam = True

    def __init__(self, config, name=None, type=None, parent=None):
	super(MethodTemplate, self).__init__(config, name=name, type=type, parent=parent)
	self.decorators = []
	self.parameters = []

    def iterDecorators(self):
	""" Yields decorators for this method. """
	def iterLines():
	    for handler in self.configHandlers('PrologueHandlers'):
		for line in handler(self):
		    yield line
	def iterOtherDecos():
	    for handler in self.configHandlers('ExtraDecoratorHandlers'):
		for line in handler(self):
		    yield line
	return chain(self.decorators, iterOtherDecos(), iterLines())

    def iterBody(self):
	""" Yields the items in the body of this template. """
	def iterDocString():
	    for handler in self.configHandlers('DocStringHandlers'):
		for line in handler(self):
		    yield self.factory.expr(left=line)
	body = list(super(MethodTemplate, self).iterBody())
	docs = list(iterDocString())
	more = [self.factory.expr(left='pass')] if not (body or docs) else []
	return chain(docs, body, more)

    def iterPrologue(self):
	""" Yields items in this method declaration, maybe with decorators. """
	for deco in self.iterDecorators():
	    yield '@{0}'.format(deco)
	firstParam = 'cls' if self.isStatic else 'self'
        first = [firstParam] if self.requiresFirstParam else []
	params = ', '.join(first + [p['name'] for p in self.parameters])
	yield 'def {0}({1}):'.format(self.name, params)


class MethodContentVisitor(BaseVisitor):
    """ MethodContentVisitor -> accepts trees for blocks within methods. """

    def acceptAssert(self, node):
	""" Accept and process an assert statement. """
	assertStat = self.factory.statement('assert', fs=FS.lsr, parent=self)
	assertStat.expr.walk(node.firstChild())

    def acceptIf(self, node):
	""" Accept and process an if statement. """
	ifStat = self.factory.statement('if', fs=FS.lsrc, parent=self)
	ifStat.expr.walk(node.firstChildOfType(tokens.PARENTESIZED_EXPR))
	blockNodes = node.childrenOfType(tokens.BLOCK_SCOPE)
	ifBlock = self.factory.methodContent(parent=self)
	ifBlock.walk(blockNodes[0])
	if len(blockNodes) == 2:
	    elseStat = self.factory.statement('else', fs=FS.lc, parent=self)
	    elseBlock = self.factory.methodContent(parent=self)
	    elseBlock.walk(blockNodes[1])

    def acceptThrow(self, node):
	""" Accept and process a throw statement. """
	throw = self.factory.statement('raise', fs=FS.lsr, parent=self)
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
        tryStat = self.factory.statement('try', fs=FS.lc, parent=self)
	tryStat.walk(tryNode)
	if catchClausesNode:
	    for catchNode in catchClausesNode.children:
		exStat = self.factory.exceptStatement('except', fs=FS.lsrc, parent=self)
		exStat.walk(catchNode)
	if finNode:
	    finStat = self.factory.statement('finally', fs=FS.lc, parent=self)
	    finStat.walk(finNode)

    def acceptExpr(self, node):
	""" Creates a new expression. """
	if node.parentType == tokens.BLOCK_SCOPE: # wrong
	    return self.factory.expr(parent=self)

    def acceptReturn(self, node):
	""" Creates a new return expression. """
	if node.parentType == tokens.BLOCK_SCOPE: # wrong
	    expr = self.factory.expr(left='return', parent=self)
	    if node.children:
		expr.fs, expr.right = FS.lsr, self.factory.expr(parent=expr)
		expr.right.walk(node)

    def acceptVarDeclaration(self, node):
	""" Creates a new expression for a variable declaration. """
	mods = node.childrenOfType(tokens.MODIFIER_LIST)
	decl = node.firstChildOfType(tokens.VAR_DECLARATOR_LIST)
	for vard in decl.childrenOfType(tokens.VAR_DECLARATOR):
	    ident = vard.firstChildOfType(tokens.IDENT)
    	    expr = vard.firstChildOfType(tokens.EXPR)
	    child = self.factory.expr(left=ident.text, parent=self)
	    assgn = child.pushRight(' = ')
	    if expr:
		assgn.walk(expr)
	    else:
		typ = node.firstChildOfType(tokens.TYPE)
		typ = typ.children[0].text
		val = assgn.pushRight()
		val.left = '{0}()'.format(typ) # wrong
	return self


class MethodVisitor(MethodContentVisitor):
    """ MethodVisitor -> accepts AST branches for method-level objects. """

    def acceptModifierList(self, node):
	""" Accept and process method modifiers. """
	if node.parentType in tokens.methodTypes:
	    self.modifiers.extend(n.text for n in node.children)
	return self

    def acceptFormalParamStdDecl(self, node):
	""" Accept and process a single parameter declaration. """
	ident = node.firstChildOfType(tokens.IDENT)

        # wrong, wrong, wrong.
	ptype = list(node.findChildrenOfType(tokens.TYPE))[0]
	try:
	    ptype = list(ptype.findChildrenOfType(tokens.IDENT))[0].text
	except:
	    ptype = ptype.firstChild().text
	ptype = self.config.combined('typeSubstitutionMap').get(ptype, ptype)

	param = {'name':ident.text, 'type':ptype}
	self.parameters.append(param)
	return self

    def acceptFormalParamVarargDecl(self, node):
	""" Accept and process a var arg declaration. """
	ident = node.firstChildOfType(tokens.IDENT)
	param = {'name':'*{0}'.format(ident.text), 'type':'A'}
	self.parameters.append(param)
	return self


class ExpressionTemplate(BaseExpressionTemplate):
    """ ExpressionTemplate -> represents a Python expression. """


class ExpressionVisitor(BaseVisitor):
    """ ClassVisitor -> accepts trees for expression objects. """

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
	expr = self.factory.expr
	self.fs = FS.l + ' ' + node.text + ' ' + FS.r
	self.left, self.right = expr(self.config, parent=self), expr(self.config)
	self.walkThisWay(node.children, (self.left, self.right))

    acceptEqual = equalityExpression
    acceptGreaterOrEqual = equalityExpression
    acceptGreaterThan = equalityExpression
    acceptLessOrEqual = equalityExpression
    acceptLessThan = equalityExpression
    acceptNotEqual = equalityExpression

    def assignExpression(self, node):
	""" Accept and processes an assignment expression (Python statement). """
	expr = self.factory.expr
	self.fs = FS.l + ' ' + node.text + ' ' + FS.r
	self.left, self.right = expr(self.config, parent=self), expr(self.config)
	self.walkThisWay(node.children, (self.left, self.right))

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

    def acceptExpr(self, node):
	""" Create a new expression within this one. """
	return self.pushRight()

    def acceptClassConstructorCall(self, node):
	""" Accept and process a class constructor call. """
	self.acceptMethodCall(node) # probably wrong

    def acceptMethodCall(self, node):
	""" Accept and process a method call. """
	expr = self.factory.expr
	self.fs = FS.l + '(' + FS.r + ')'
	self.left, self.right = expr(parent=self), expr(parent=self)
	self.left.walk(node.firstChild())
	self.right.walk(node.firstChildOfType(tokens.ARGUMENT_LIST))

    def acceptDot(self, node):
	""" Accept and process a dotted expression. """
	expr = self.factory.expr
	self.fs = FS.l + '.' + FS.r
	self.left, self.right = expr(parent=self), expr(parent=self)
	self.walkThisWay(node.children, (self.left, self.right))

    def acceptQuestion(self, node):
	""" Accept and process a terinary expression. """
	expr = self.factory.expr
	self.fs = FS.l + ' if ' + FS.r
	self.left = expr(parent=self)
	self.right = expr(fs=FS.l+' else '+FS.r, parent=self)
        self.right.left = expr(parent=self.right)
	self.right.right = expr(parent=self.right)
	self.walkThisWay(node.children, (self.right.left, self.left, self.right.right))

    def pushRight(self, value=''):
	""" Creates a new right expression, sets it, and returns it. """
	self.right = self.factory.expr(left=value, parent=self)
	return self.right


class StatementTemplate(BaseTemplate):
    """ StatementTemplate -> template type for generating Python statements. """

    def __init__(self, config, keyword, fs=FS.lr, parent=None):
	super(StatementTemplate, self).__init__(config, parent=parent)
	self.keyword = keyword
	self.expr = self.factory.expr(left=keyword, fs=fs)

    def __repr__(self):
	""" Returns the debug string representation of this template. """
	parts = [green('statement'), white('keyword:')+cyan(self.keyword)]
	return ' '.join(parts)

    def iterPrologue(self):
	""" Yields the keyword (and clause, if any) for this statement . """
	yield self.expr


class StatementVisitor(MethodContentVisitor):
    """ StatementVisitor -> accepts AST branches for statement objects. """


class ExceptStatementVisitor(MethodContentVisitor):
    """ ExceptStatementVisitor -> accepts AST branches for 'except' statements. """

    def acceptCatch(self, node):
	""" Accept and process a catch statement. """
	decl = node.firstChildOfType(tokens.FORMAL_PARAM_STD_DECL)
	dtype = decl.firstChildOfType(tokens.TYPE)
	tnames = dtype.findChildrenOfType(tokens.IDENT)
	cname = '.'.join(n.text for n in tnames)
	cname = self.config.combined('exceptionSubMap').get(cname, cname)
	cvar = decl.firstChildOfType(tokens.IDENT)
	block = node.firstChildOfType(tokens.BLOCK_SCOPE)
	self.expr.fs = FS.lsrc
	self.expr.right = Expression(self.config, fs=FS.l+' as '+FS.r, left=cname, right=cvar)
	self.walk(block)


class Module(ModuleTemplate, ModuleVisitor):
    """ Module -> represents a Python module. """
    factoryTypeName = 'module'


class Class(ClassTemplate, ClassVisitor):
    """ Class -> represents a Python class. """
    factoryTypeName = 'klass'


class Method(MethodTemplate, MethodVisitor):
    """ Method -> represents a Python method. """
    factoryTypeName = 'method'


class MethodContent(BaseTemplate, MethodContentVisitor):
    """ MethodContent -> represents content within a Python method. """
    factoryTypeName = 'methodContent'


class Expression(ExpressionTemplate, ExpressionVisitor):
    """ Expression -> represents a Python expression. """
    factoryTypeName = 'expr'


class Statement(StatementTemplate, StatementVisitor):
    """ Statement -> represents a Python statement. """
    factoryTypeName = 'statement'


class ExceptStatement(StatementTemplate, ExceptStatementVisitor):
    """ ExceptStatement -> represents a Python 'except' statement. """
    factoryTypeName = 'exceptStatement'
