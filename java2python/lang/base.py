#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# recognizers: lexer, parser, treeparser
# streams: string, file name, file handle
#
# Parsers use TokenStreams (CommonTokenStream or TokenRewriteStream)
#
# Tree parsers use TreeNodeStream (CommonTreeNodeStream)
#
# Lexers emit Token objects (buffered in TokenStream objects)
#
# Parsers build trees if their output is AST.
#
# token types: CommonToken and ClassicToken.  Our tree adaptor
# creates LocalTokens instead.
#
# Tree (CommonTree) wraps Token objects.  We provide extra functionality via
# the LocalTree class.
#
# TreeAdaptor (CommonTreeAdaptor) is used by the parser to create
# Tree objects.  Our adaptor, LocalTreeAdaptor, creates the LocalTree
# instances.
#
##
import types
from keyword import kwlist
from antlr3 import ANTLRStringStream, CommonTokenStream, Lexer, Parser
from antlr3.tree import CommonTreeAdaptor, CommonTree
from java2python.lib import colortools


class Tokens(object):
    """ Tokens -> simplifies token id-name and name-id mapping. """

    def __init__(self):
	self.cache, self.parserModule = {}, None

    def __getattr__(self, name):
	return getattr(self.module, name)

    @property
    def commentTypes(self):
	return (self.module.COMMENT, self.module.LINE_COMMENT, )

    @property
    def methodTypes(self):
        return (self.module.VOID_METHOD_DECL, self.module.FUNCTION_METHOD_DECL)

    @property
    def map(self):
	cache, module = self.cache, self.module
	if cache:
	    return cache
	mapping = [(getattr(module, k, None), k) for k in module.tokenNames]
	mapping = [(k, v) for k, v in mapping if k is not None]
	cache.update(mapping)
	return cache

    @property
    def module(self):
	module = self.parserModule
	if module is None:
	    import java2python.lang.JavaParser as module
	    self.parserModule = module
	return module

    @staticmethod
    def title(name):
	return ''.join(part.title() for part in name.split('_'))


tokens = Tokens()


## TODO:  switch on string/file-like
class LocalSourceStream(ANTLRStringStream):
    pass


class LocalTokenStream(CommonTokenStream):
    pass


class LocalRecognizer(object):
    pass


class LocalParser(Parser, LocalRecognizer):
    def __init__(self, input, state=None):
	super(LocalParser, self).__init__(input, state=state)


def typeNames():
    typs = [getattr(types, n) for n in dir(types) if not n.startswith('_')]
    names = [t.__name__ for t in typs if isinstance(t, type)]
    return ['None', 'True', 'False', ] + names


def transformConstMethod(v):
    def transformMethod(self, node):
	node.token.text = v
    return transformMethod


class LocalLexer(Lexer, LocalRecognizer):
    renameIdents = kwlist + typeNames()

    def __init__(self, input=None, state=None):
	super(LocalLexer, self).__init__(input, state)

    def transform(self, node):
	title = tokens.title(tokens.map.get(node.token.type, ''))
	if title:
	    call = getattr(self, 'transform{0}'.format(title), lambda n:None)
	    call(node)

    transformFalse = transformConstMethod('False')
    transformTrue = transformConstMethod('True')
    transformNull = transformConstMethod('None')

    def transformIdent(self, node):
	ident = node.token.text
	node.token.text = '%s_' % ident if ident in self.renameIdents else ident

    def transformFloatingPointLiteral(self, node):
	value = node.token.text
        if value.startswith('.'):
            value = '0' + value
        if value.endswith(('f', 'd')):
            value = value[:-1]
        elif value.endswith(('l', 'L')):
            value = value[:-1] + 'L'
	node.token.text = value


class LocalTree(CommonTree):
    colorTypeMap = {
	'CLASS'            : colortools.green,
	'JAVA_SOURCE'      : colortools.green,
	'VOID_METHOD_DECL' : colortools.green,
	'IDENT'            : colortools.yellow,
	'TYPE'             : colortools.magenta,
	'EXPR'             : colortools.blue,
	'TRUE'             : colortools.yellow,
	'FALSE'            : colortools.yellow,
	'NULL'             : colortools.yellow,
    }

    def colorType(self, tokenType):
	return self.colorTypeMap.get(tokenType, colortools.white)(tokenType)

    def colorText(self, tokenType, tokenText):
	return self.colorTypeMap.get(tokenType, colortools.white)(tokenText)

    def colorComments(self, token):
	ttyp = tokens.map.get(token.type)
	text = token.text.replace('\n', '\\n').replace('\r', '\\r').replace('\t', '\\t')
	item = '{0} [{1}:{2}] {3}'.format(ttyp, token.start, token.stop, text)
	yield colortools.black(item)

    def dump(self, fd, level=0):
	extras = lambda x, y:x and (x != y)
	seen, nform = set(), '{0}{1}{2}{3}'

	def innerDump(root, offset):
	    token, indent = root.token, '    ' * offset
	    start, stop = root.tokenStartIndex, root.tokenStopIndex
	    idxes, ttyp = '', tokens.map.get(token.type, '?')
	    if start and stop and start == stop:
		idxes = ' [{0}]'.format(start)
	    elif start and stop:
	        idxes = ' [{0}:{1}]'.format(start, stop)
	    args = [indent, self.colorType(ttyp), '', idxes, '']
	    if extras(token.text, ttyp):
		args[2] = ' ' + self.colorText(ttyp, token.text)
	    for com in self.selectComments(start, seen):
		for line in self.colorComments(com):
		    print >> fd, '{0}{1}'.format(indent, line)
	    print >> fd, nform.format(*args)
	    for child in root.getChildren():
		innerDump(child, offset+1)
	    for com in self.selectComments(root.tokenStopIndex, seen):
		for line in self.colorComments(com):
		    print >> fd, '{0}{1}'.format(indent, line)
	innerDump(self, level)

    def selectComments(self, stop, memo):
	pred = lambda k:k.type in tokens.commentTypes and k.index not in memo
	ctoks = [t for t in self.parser.input.tokens[0:stop] if pred(t)]
	memo.update(t.index for t in ctoks)
	return ctoks

    def childrenOfType(self, type):
	return (c for c in self.children if c.type==type)

    def firstChild(self, default=None):
	try:
	    return self.children[0]
	except (IndexError, ):
	    return default

    def firstChildOfType(self, type, default=None):
	for child in self.children:
	    if child.type == type:
		return child
	return default

    def findChildren(self, pred=lambda c:True):
	""" Depth-first search that yields nodes meeting the predicate. """
	for child in self.children:
	    if pred(child):
		yield child
	    for sub in child.findChildren(pred):
		yield sub

    def findChildrenOfType(self, type):
	""" Depth-first search that yields nodes of the given type. """
	return self.findChildren(lambda c:c.type==type)

    @property
    def parentType(self):
	""" Returns the type of the parent node. """
	return self.parent.type

    def dupNode(self):
	node = LocalTree(self)
	node.parser = getattr(self, 'parser', None)
	node.lexer = getattr(self, 'lexer', None)
	return node

    @property
    def parserTokens(self):
	return self.parser.input.tokens[self.tokenStartIndex:self.tokenStopIndex]

    def select(self, selector):
	pass



class LocalTreeAdaptor(CommonTreeAdaptor):
    treeType = LocalTree

    def __init__(self, callback=None):
	CommonTreeAdaptor.__init__(self)
	self.callback = callback

    def createWithPayload(self, payload):
        node = self.treeType(payload)
	if node.token and self.callback:
	    self.callback(node)
	return node
