#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" java2python.compiler.visitor -> Base classes for walking ASTs. """
##
#
# This module defines the base visitor class, Base.  It
# implements the accept() and walk() methods.  The walk() method
# handles finding and inserting blocks for hidden comment lexer nodes.
#
from functools import reduce
from itertools import ifilter, izip, tee
from re import compile as rxcompile, sub as rxsub

from java2python.lang import tokens
from java2python.lib import FS


class Memo(object):
    """ Memo -> AST walking luggage. """
    def __init__(self):
	self.comments, self.last = set(), 0


class Base(object):
    """ Base -> Base class for AST visitors. """
    commentSubs = (
	rxcompile('^\s*/(\*)+'), rxcompile('(\*)+/\s*$'), rxcompile('^\s*//'),
    )

    def accept(self, node, memo):
	""" Accept a node, possibly creating a child visitor. """
	title = tokens.title(tokens.map.get(node.token.type))
	call = getattr(self, 'accept{0}'.format(title), lambda n, m:self)
        return call(node, memo)

    def walk(self, tree, memo=None):
	""" Depth-first visiting of the given AST. """
	if not tree:
	    return
	memo = Memo() if memo is None else memo
	self.insertComments(self, tree, tree.tokenStartIndex, memo)
	visitor = self.accept(tree, memo)
	if visitor:
	    for child in tree.children:
		visitor.walk(child, memo)
		self.insertComments(visitor, child, child.tokenStopIndex, memo)
	self.insertComments(self, tree, tree.tokenStopIndex, memo)
	## we've got to cheat and check to see if this is a
	## compilation unit node.  if so, scan any remaining tokens.
	if tree.token.type == tokens.JAVA_SOURCE:
	    self.insertComments(self, tree, len(tree.parser.input.tokens), memo)

    def zipWalk(self, nodes, visitors, memo):
	""" Walk the given nodes zipped with the given visitors. """
	for node, visitor in izip(nodes, visitors):
	    visitor.walk(node, memo)

    def insertComments(self, block, tree, index, memo):
	""" Add comments to the block from tokens in the tree. """
	cache, parser = memo.comments, tree.parser
	prefix = self.config.last('commentPrefix', '# ')

	## the next for loop should read like this, but it's pretty
	## slow that way:
	#
	#pred = lambda k:k.type in tokens.commentTypes and k.index not in cache
	#for token in ifilter(pred, parser.input.tokens[0:index]):
	for token in parser.input.tokens[memo.last:index]:
	    if token.type not in tokens.commentTypes or token.index in cache:
		continue
	    cache.add(token.index)
	    isexp = getattr(block, 'isExpression', False)
	    if isexp and (token.line == parser.input.tokens[index].line):
  	        block.tail += '' if block.tail.startswith(prefix) else prefix
		block.tail += ''.join(self.stripComment(token.text))
	    else:
		for line in self.stripComment(token.text):
		    self.factory.comment(left=prefix, right=line, parent=self)
	memo.last = index

    def stripComment(self, text):
	""" Regex substitutions for comments; removes comment characters. """
	resub = lambda val, rx:rxsub(rx, '', val)
	for text in ifilter(unicode.strip, text.split('\n')):
	    yield reduce(resub, self.commentSubs, text)


class ModuleClassSharedMixin(object):
    """ ModuleClassSharedMixin -> shared visitor methods for type declarations """

    def makeAcceptType(ft):
	def accept(self, node, memo):
	    name = node.firstChildOfType(tokens.IDENT).text
	    self.variables.append(name)
	    return getattr(self.factory, ft)(name=name, parent=self)
	return accept

    acceptAt = makeAcceptType('at')
    acceptClass = makeAcceptType('klass')
    acceptEnum = makeAcceptType('enum')
    acceptInterface = makeAcceptType('interface')

class Module(ModuleClassSharedMixin, Base):
    """ Module -> accepts AST branches for module-level objects. """


class ClassMethodSharedMixin(object):
    def acceptModifierList(self, node, memo):
	""" Accept and process class and method modifiers. """
	## this is pretty bad.  wrong.
	for mod in node.children:
	    if mod.type == tokens.AT:
		## needs args, too
		deco = '{0}()'.format(mod.firstChildOfType(tokens.IDENT).text)
		self.decorators.append(deco)
	    else:
		if node.parentType in tokens.methodTypes:
		    self.modifiers.extend(n.text for n in node.children) ## wrong
		    if self.isStatic:
			self.parameters[0]['name'] = 'cls'
		self.modifiers.append(mod.text)
	return self





class Class(ModuleClassSharedMixin, ClassMethodSharedMixin, Base):
    """ Class -> accepts AST branches for class-level objects. """

    def acceptAt(self, node, memo):
	""" Accept and ignore an annotation declaration. """
	## this overrides the ModuleClassSharedMixin implementation and
	## ignores AT tokens; they're sent within the class modifier
	## list and we have no use for them here.


    def acceptConstructorDecl(self, node, memo):
	""" Accept and process a constructor declaration. """
	method = self.factory.method(name='__init__', type=self.name, parent=self)
	superCalls = node.findChildrenOfType(tokens.SUPER_CONSTRUCTOR_CALL)
	if not any(superCalls) and any(self.bases):
	    ## from the java tutorial:
	    # Note: If a constructor does not explicitly invoke a
	    # superclass constructor, the Java compiler automatically
	    # inserts a call to the no-argument constructor of the
	    # superclass.
	    fs = 'super(' + FS.r + ', self).__init__()'
	    self.factory.expr(fs=fs, right=self.name, parent=method)
	return method

    def acceptExtendsClause(self, node, memo):
	""" Accept and process an extends clause. """
	names = (n.text for n in node.findChildrenOfType(tokens.IDENT))
	self.bases.extend(names)

    def acceptFunctionMethodDecl(self, node, memo):
	""" Accept and process a typed method declaration. """
	ident = node.firstChildOfType(tokens.IDENT)
	type = node.firstChildOfType(tokens.TYPE).children[0].text
	return self.factory.method(name=ident.text, type=type, parent=self)

    acceptImplementsClause = acceptExtendsClause


    def acceptVarDeclaration(self, node, memo):
	""" Creates a new expression for a variable declaration. """
	## this is strikingly similar to
	## MethodContent.acceptVarDeclaration; merge and fix.

	decl = node.firstChildOfType(tokens.VAR_DECLARATOR_LIST)
	for vard in decl.childrenOfType(tokens.VAR_DECLARATOR):
	    ident = vard.firstChildOfType(tokens.IDENT)
	    self.variables.append(ident.text)
    	    expr = vard.firstChildOfType(tokens.EXPR)
	    child = self.factory.expr(left=ident.text, parent=self)
	    assgn = child.pushRight(' = ')
	    arinit = vard.firstChildOfType(tokens.ARRAY_INITIALIZER)
	    if arinit:
		assgn.right = exp = self.factory.expr(fs='['+FS.lr+']', parent=child)
		children = list(arinit.childrenOfType(tokens.EXPR))
		for c in children:
		    fs = FS.lr if c is children[-1] else FS.lr + ', '
		    exp.left = self.factory.expr(fs=fs, parent=child)
		    exp.left.walk(c, memo)
		    exp.right = exp = self.factory.expr(parent=child)
	    elif expr:
		assgn.walk(expr, memo)
	    else:
		typ = node.firstChildOfType(tokens.TYPE)
		typ = typ.children[0].text
		val = assgn.pushRight()
		val.left = '{0}()'.format(typ) # wrong
	return self

    def acceptVoidMethodDecl(self, node, memo):
	""" Accept and process a void method declaration. """
	ident = node.firstChildOfType(tokens.IDENT)
	return self.factory.method(name=ident.text, type='void', parent=self)

class Annotation(Class):
    """ Annotation -> accepts AST branches for Java annotations. """
    def acceptAnnotationMethodDecl(self, node, memo):
	""" Accept and process an annotation method declaration. """
	ident = node.firstChildOfType(tokens.IDENT)
	type = node.firstChildOfType(tokens.TYPE).children[0].text
	return self.factory.method(name=ident.text, type=type, parent=self)


class Enum(Class):
    """ Enum -> accepts AST branches for Java enums. """

    def acceptEnumTopLevelScope(self, node, memo):
	""" Accept and process an enum scope """
	idents = node.childrenOfType(tokens.IDENT)
	expr = self.factory.expr
	clsset = lambda v:'{0}.{1} = {2}'.format(self.name, v, self.name)
	handler = self.configHandler('Value')
	for index, ident in enumerate(idents):
	    if list(ident.findChildrenOfType(tokens.ARGUMENT_LIST)):
		call = expr(left=clsset(ident), parent=self.parent)
		call.right = arg = expr(fs='('+FS.lr+')')
		argl = ident.firstChildOfType(tokens.ARGUMENT_LIST)
		exprs = list(argl.findChildrenOfType(tokens.EXPR))
		for ex in exprs:
		    arg.left = expr(fs=FS.r + (', ' if ex != exprs[-1] else ''))
		    arg.left.walk(ex, memo)
		    arg.right = arg = expr()
	    else:
		value = expr(fs=ident.text+' = '+FS.r, parent=self)
		value.pushRight(handler(self, index, ident.text))
	return self




class Interface(Class):
    """ Interface -> accepts AST branches for Java interfaces. """




class MethodContent(Base):
    """ MethodContent -> accepts trees for blocks within methods. """

    def acceptBreak(self, node, memo):
	""" Accept and process a break statement. """
	if node.parent and node.parent.type in (tokens.CASE, tokens.DEFAULT):
	    return
	breakStat = self.factory.statement('break', parent=self)

    def acceptWhile(self, node, memo):
	""" Accept and process a while block. """
	# WHILE - PARENTESIZED_EXPR - BLOCK_SCOPE
	parNode, blkNode = node.children
	whileStat = self.factory.statement('while', fs=FS.lsrc, parent=self)
	whileStat.expr.walk(parNode, memo)
	whileStat.walk(blkNode, memo)

    def acceptDo(self, node, memo):
	""" Accept and process a do-while block. """
	# DO - BLOCK_SCOPE - PARENTESIZED_EXPR
	blkNode, parNode = node.children
	whileStat = self.factory.statement('while', fs=FS.lsrc, parent=self)
	whileStat.expr.right = 'True'
	whileStat.walk(blkNode, memo)
	fs = FS.l+ ' ' + 'not ({right}):'
	ifStat = self.factory.statement('if', fs=fs, parent=whileStat)
	ifStat.expr.walk(parNode, memo)
	breakStat = self.factory.statement('break', parent=ifStat)

    def acceptSwitch(self, node, memo):
	""" Accept and process a switch block. """
	# This implementation needs a lot of work to handle case
	# statements without breaks, out-of-order default labels, etc.
	# Given the current size and complexity, consider growing a
	# Case block type.
	parNode = node.firstChildOfType(tokens.PARENTESIZED_EXPR)
	lblNode = node.firstChildOfType(tokens.SWITCH_BLOCK_LABEL_LIST)
	caseNodes = lblNode.children
        ## empty switch statement
	if not len(caseNodes):
	    return
	## we have at least one node...
	parExpr = self.factory.expr()
	parExpr.walk(parNode)
	eqFs = FS.l + '==' + FS.r
	for caseIdx, caseNode in enumerate(caseNodes):
	    isDefault, isFirst = caseNode.type==tokens.DEFAULT, caseIdx==0

	    if isFirst:
   	        caseExpr = self.factory.statement('if', fs=FS.lsrc, parent=self)
	    elif not isDefault:
		caseExpr = self.factory.statement('elif', fs=FS.lsrc, parent=self)
	    elif isDefault:
		caseExpr = self.factory.statement('else', fs=FS.lc, parent=self)

	    if not isDefault:
		right = self.factory.expr()
		right.walk(caseNode.firstChildOfType(tokens.EXPR))
		caseExpr.expr.right = self.factory.expr(left=parExpr, right=right, fs=eqFs)
		caseContent = self.factory.methodContent(parent=self)
		for child in caseNode.children[1:]:
		    caseContent.walk(child, memo)
		if not caseNode.children[1:]:
		    self.factory.expr(left='pass', parent=caseContent)
	    if isDefault:
		if isFirst:
		    caseExpr.expr.right = 'True'
		caseContent = self.factory.methodContent(parent=self)
		for child in caseNode.children:
		    caseContent.walk(child, memo)
		if not caseNode.children:
		    self.factory.expr(left='pass', parent=caseContent)

    def acceptCatch(self, node, memo):
	""" Accept and process a catch statement. """
	decl = node.firstChildOfType(tokens.FORMAL_PARAM_STD_DECL)
	dtype = decl.firstChildOfType(tokens.TYPE)
	tnames = dtype.findChildrenOfType(tokens.IDENT)
	cname = '.'.join(n.text for n in tnames)
	cvar = decl.firstChildOfType(tokens.IDENT)
	block = node.firstChildOfType(tokens.BLOCK_SCOPE)
	self.expr.fs = FS.lsrc
	self.expr.right = self.factory.expr(fs=FS.l+' as '+FS.r, left=cname, right=cvar)
	self.walk(block, memo)

    def acceptAssert(self, node, memo):
	""" Accept and process an assert statement. """
	assertStat = self.factory.statement('assert', fs=FS.lsr, parent=self)
	assertStat.expr.walk(node.firstChild(), memo)

    def acceptIf(self, node, memo):
	""" Accept and process an if statement. """
	## the parser will feed us one of three forms:
	## bare if:          PARENTESIZED_EXPR - BLOCK_SCOPE
	## if with else:     PARENTESIZED_EXPR - BLOCK_SCOPE - BLOCK_SCOPE
	## if with else if:  PARENTESIZED_EXPR - BLOCK_SCOPE - IF
	children = node.children
	ifStat = self.factory.statement('if', fs=FS.lsrc, parent=self)
	ifStat.expr.walk(children[0], memo)
	ifBlock = self.factory.methodContent(parent=self)
	ifBlock.walk(node.children[1], memo)
	if len(children) == 3:
	    nextNode = children[2]
	    nextType = nextNode.type
	    while nextType == tokens.IF:
		nextStat = self.factory.statement('elif', fs=FS.lsrc, parent=self)
		nextStat.expr.walk(nextNode.children[0], memo)
		nextBlock = self.factory.methodContent(parent=self)
		nextBlock.walk(nextNode.children[1], memo)
		try:
		    nextNode = nextNode.children[2]
		    nextType = nextNode.type
		except (IndexError, ):
		    nextType = None
	    if nextType == tokens.BLOCK_SCOPE:
		self.factory.statement('else', fs=FS.lc, parent=self)
		self.factory.methodContent(parent=self).walk(nextNode, memo)

    def acceptThrow(self, node, memo):
	""" Accept and process a throw statement. """
	throw = self.factory.statement('raise', fs=FS.lsr, parent=self)
	throw.expr.walk(node.children[0], memo)

    def acceptTry(self, node, memo):
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
	tryStat.walk(tryNode, memo)
	if catchClausesNode:
	    for catchNode in catchClausesNode.children:
		exStat = self.factory.statement('except', fs=FS.lsrc, parent=self)
		exStat.walk(catchNode, memo)
	if finNode:
	    finStat = self.factory.statement('finally', fs=FS.lc, parent=self)
	    finStat.walk(finNode, memo)

    def acceptExpr(self, node, memo):
	""" Creates a new expression. """
	goodParents = (tokens.BLOCK_SCOPE, tokens.CASE, tokens.DEFAULT, tokens.FOR_EACH)
	if node.parentType in goodParents: # wrong
	    return self.factory.expr(parent=self)

    def acceptReturn(self, node, memo):
	""" Creates a new return expression. """
	if node.parentType == tokens.BLOCK_SCOPE: # wrong
	    expr = self.factory.expr(left='return', parent=self)
	    if node.children:
		expr.fs, expr.right = FS.lsr, self.factory.expr(parent=expr)
		expr.right.walk(node, memo)

    def acceptVarDeclaration(self, node, memo):
	""" Creates a new expression for a variable declaration. """
	varDecls = node.firstChildOfType(tokens.VAR_DECLARATOR_LIST)
	for varDecl in varDecls.childrenOfType(tokens.VAR_DECLARATOR):
	    ident = varDecl.firstChildOfType(tokens.IDENT)
	    self.variables.append(ident.text)
	    identExp = self.factory.expr(left=ident.text, parent=self)
	    assgnExp = identExp.pushRight(' = ')
	    declExp = varDecl.firstChildOfType(tokens.EXPR)
	    declArr = varDecl.firstChildOfType(tokens.ARRAY_INITIALIZER)
	    if declExp:
		assgnExp.walk(declExp, memo)
            elif declArr:
		assgnExp.right = exp = self.factory.expr(fs='['+FS.lr+']')
		children = list(declArr.childrenOfType(tokens.EXPR))
		for child in children:
		    fs = FS.lr if child is children[-1] else FS.lr + ', '
		    exp.left = self.factory.expr(fs=fs)
		    exp.left.walk(child, memo)
		    exp.right = exp = self.factory.expr()
	    else:
		if node.firstChildOfType(tokens.TYPE).firstChildOfType(tokens.ARRAY_DECLARATOR_LIST):
		    val = assgnExp.pushRight()
		    val.left = '[]'
		else:
		    typ = node.firstChildOfType(tokens.TYPE)
		    typ = typ.children[0].text
		    val = assgnExp.pushRight()
		    val.left = '{0}()'.format(typ) # wrong
	return self

    def acceptForEach(self, node, memo):
	""" Accept and process a 'for each' style statement. """
	forEach = self.factory.statement('for', fs=FS.lsrc, parent=self)
	identExpr = forEach.expr.right = self.factory.expr(fs=FS.l+' in '+FS.r)
	identExpr.walk(node.firstChildOfType(tokens.IDENT), memo)
	inExpr = identExpr.right = self.factory.expr()
	inExpr.walk(node.firstChildOfType(tokens.EXPR), memo)
	forBlock = self.factory.methodContent(parent=self)
	#print '############', [tokens.map[n.type] for n in node.children]
	#forBlock.walk(node.firstChildOfType(tokens.BLOCK_SCOPE), memo)
	forBlock.walk(node.children[4], memo)

    def acceptFor(self, node, memo):
	""" Accept and process a 'for' statement. """
	self.walk(node.firstChildOfType(tokens.FOR_INIT))
	whileStat = self.factory.statement('while', fs=FS.lsrc, parent=self)
	whileStat.expr.walk(node.firstChildOfType(tokens.FOR_CONDITION))
	whileBlock = self.factory.methodContent(parent=self)
	whileBlock.walk(node.firstChildOfType(tokens.BLOCK_SCOPE))
	updateStat = self.factory.expr(parent=whileBlock)
	updateStat.walk(node.firstChildOfType(tokens.FOR_UPDATE))


class Method(ClassMethodSharedMixin, MethodContent):
    """ Method -> accepts AST branches for method-level objects. """

    def acceptFormalParamStdDecl(self, node, memo):
	""" Accept and process a single parameter declaration. """
	ident = node.firstChildOfType(tokens.IDENT)

        # wrong, wrong, wrong.
	ptype = list(node.findChildrenOfType(tokens.TYPE))[0]
	try:
	    ptype = list(ptype.findChildrenOfType(tokens.IDENT))[0].text
	except (IndexError, ):
	    ptype = ptype.firstChild().text
	self.parameters.append(self.makeParam(ident.text, ptype))
	return self

    def acceptFormalParamVarargDecl(self, node, memo):
	""" Accept and process a var arg declaration. """
	ident = node.firstChildOfType(tokens.IDENT)
	param = {'name':'*{0}'.format(ident.text), 'type':'A'}
	self.parameters.append(param)
	return self


class Expression(Base):
    """ Class -> accepts trees for expression objects. """

    def textExpression(self, node, memo):
	""" Assigns node text to the left side of this expression. """
	self.left = node.text

    acceptCharacterLiteral = textExpression
    acceptStringLiteral = textExpression
    acceptFloatingPointLiteral = textExpression
    acceptDecimalLiteral = textExpression
    acceptHexLiteral = textExpression
    acceptOctalLiteral = textExpression
    acceptTrue = textExpression
    acceptFalse = textExpression
    acceptNull = textExpression

    def equalityExpression(self, node, memo):
	""" Accept and processes an equality expression. """
	expr = self.factory.expr
	self.fs = FS.l + ' ' + node.text + ' ' + FS.r
	self.left, self.right = visitors = expr(parent=self), expr()
	self.zipWalk(node.children, visitors, memo)

    acceptEqual = equalityExpression
    acceptGreaterOrEqual = equalityExpression
    acceptGreaterThan = equalityExpression
    acceptLessOrEqual = equalityExpression
    acceptLessThan = equalityExpression
    acceptNotEqual = equalityExpression
    acceptOr = equalityExpression
    acceptXor = equalityExpression
    acceptAnd = equalityExpression
    acceptShiftRight = equalityExpression
    acceptShiftLeft = equalityExpression
    acceptMod = equalityExpression

    def acceptBitShiftRight(self, node, memo):
	expr = self.factory.expr
	self.fs = 'bsr(' + FS.l + ', ' + FS.r + ')'
	self.left, self.right = visitors = expr(parent=self), expr()
	self.zipWalk(node.children, visitors, memo)
	module = self.parents(lambda x:x.isModule).next()
	module.needsBsrFunc = True

    def acceptBitShiftRightAssign(self, node, memo):
	expr = self.factory.expr
	self.fs = FS.l + ' = bsr(' + FS.l + ', ' + FS.r + ')'
	self.left, self.right = visitors = expr(parent=self), expr()
	self.zipWalk(node.children, visitors, memo)
	module = self.parents(lambda x:x.isModule).next()
	module.needsBsrFunc = True

    def assignExpression(self, node, memo):
	""" Accept and processes an assignment expression (Python statement). """
	expr = self.factory.expr
	self.fs = FS.l + ' ' + node.text + ' ' + FS.r
	self.left, self.right = visitors = expr(parent=self), expr()
	self.zipWalk(node.children, visitors, memo)

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

    def acceptExpr(self, node, memo):
	""" Create a new expression within this one. """
	return self.pushRight()

    def acceptIdent(self, node, memo):
	""" Accept and process an ident expression. """
	self.left = name = self.altIdent(node.text)

    def acceptInstanceof(self, node, memo):
	""" Accept and process an instanceof expression. """
	self.fs = 'isinstance({right}, ({left}, ))'
	self.right = self.factory.expr(parent=self)
	self.right.walk(node.firstChildOfType(tokens.IDENT), memo)
	self.left = self.factory.expr(parent=self)
	self.left.walk(node.firstChildOfType(tokens.TYPE), memo)

    def acceptClassConstructorCall(self, node, memo):
	""" Accept and process a class constructor call. """
	self.acceptMethodCall(node, memo) # probably wrong

    def acceptMethodCall(self, node, memo):
	""" Accept and process a method call. """
	## note: this creates one too many expression levels.
	expr = self.factory.expr
	self.fs = FS.l + '(' + FS.r + ')'
	self.left = expr(parent=self)
	self.left.walk(node.firstChild(), memo)
	children = node.firstChildOfType(tokens.ARGUMENT_LIST).children
	self.right = arg = expr(parent=self)
	for child in children:
	    fs = FS.r + (', ' if child is not children[-1] else '')
	    arg.left = expr(fs=fs, parent=self)
	    arg.left.walk(child, memo)
	    arg.right = arg = expr(parent=self)

    def acceptDot(self, node, memo):
	expr = self.factory.expr
	self.fs = FS.l + '.' + FS.r
	self.left, self.right = visitors = expr(), expr()
	self.zipWalk(node.children, visitors, memo)

    def makeAcceptPreFormatted(fs):
	def accept(self, node, memo):
	    expr = self.factory.expr
	    self.fs = fs
	    self.left, self.right = vs = expr(parent=self), expr(parent=self)
	    self.zipWalk(node.children, vs, memo)
	return accept

    acceptArrayElementAccess = makeAcceptPreFormatted(FS.l + '[' + FS.r + ']')
    acceptDiv = makeAcceptPreFormatted(FS.l + ' / ' + FS.r)
    acceptLogicalAnd = makeAcceptPreFormatted(FS.l + ' and ' + FS.r)
    acceptLogicalOr  = makeAcceptPreFormatted(FS.l + ' or ' + FS.r)
    acceptLogicalNot  = makeAcceptPreFormatted('not ' + FS.l)

    acceptMinus = makeAcceptPreFormatted(FS.l + ' - ' + FS.r)
    acceptPlus = makeAcceptPreFormatted(FS.l + ' + ' + FS.r)
    acceptStar = makeAcceptPreFormatted(FS.l + ' * ' + FS.r)
    acceptUnaryPlus = makeAcceptPreFormatted('+' + FS.l)
    acceptUnaryMinus = makeAcceptPreFormatted('-' + FS.l)
    acceptNot = makeAcceptPreFormatted('~' + FS.l)

    ## wrong.
    acceptCastExpr  = makeAcceptPreFormatted(FS.l + '(' + FS.r + ')' )

    def makeAcceptPrePost(suffix, pre=False):
	def accept(self, node, memo):
	    expr = self.factory.expr
	    if node.withinExpr:
		ident = node.firstChildOfType(tokens.IDENT).text
		handler = self.configHandler('VariableNaming')
		name = handler(ident)
		block = self.parents(lambda x:x.isMethod).next()
		if pre:
		    left = ident
		else:
		    left = name
		    block.insertChild(expr(fs=FS.l+' = '+FS.r, left=name, right=ident))
		self.left = expr(parent=self, fs=FS.l, left=left)
		block.insertChild(expr(fs=FS.l + suffix, left=ident))
	    else:
		self.fs = FS.l + suffix
		self.left, self.right = vs = expr(parent=self), expr(parent=self)
		self.zipWalk(node.children, vs, memo)
	return accept

    acceptPostInc = makeAcceptPrePost(' += 1')
    acceptPreInc = makeAcceptPrePost(' += 1', pre=True)
    acceptPostDec = makeAcceptPrePost(' -= 1')
    acceptPreDec = makeAcceptPrePost(' -= 1', pre=True)

    def acceptSuperConstructorCall(self, node, memo):
	cls = self.parents(lambda c:c.isClass).next()
	fs = 'super(' + FS.l + ', self).__init__(' + FS.r + ')'
	self.right = self.factory.expr(fs=fs, left=cls.name)
	return self.right

    def acceptStaticArrayCreator(self, node, memo):
	self.right = self.factory.expr(fs='[None]*{left}')
	self.right.left = self.factory.expr()
	self.right.left.walk(node.firstChildOfType(tokens.EXPR), memo)

    def acceptThis(self, node, memo):
	self.pushRight('self')

    def acceptQuestion(self, node, memo):
	""" Accept and process a terinary expression. """
	expr = self.factory.expr
	self.fs = FS.l + ' if ' + FS.r
	self.left = expr(parent=self)
	self.right = expr(fs=FS.l+' else '+FS.r, parent=self)
        self.right.left = expr(parent=self.right)
	self.right.right = expr(parent=self.right)
	visitors = (self.right.left, self.left, self.right.right)
	self.zipWalk(node.children, visitors, memo)

    def pushRight(self, value=''):
	""" Creates a new right expression, sets it, and returns it. """
	self.right = self.factory.expr(left=value, parent=self)
	return self.right


class Comment(Expression):
    """ """

class Statement(MethodContent):
    """ Statement -> accepts AST branches for statement objects. """
