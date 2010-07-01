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

from keyword import kwlist
from antlr3 import ANTLRStringStream, CommonTokenStream, Lexer, Parser
from antlr3.tree import CommonTreeAdaptor, CommonTree
from java2python.lib import colortools


class Tokens(object):
    def __init__(self):
	self.cache = {}

    def __getattr__(self, name):
	return getattr(self.module, name)

    @property
    def commentTypes(self):
	return (self.module.COMMENT, self.module.LINE_COMMENT)

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
	import java2python.parser.JavaParser as module
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
    def setComments(self, comments):
	self.comments = comments

    def addComment(self, start, stop, text):
        self.comments.append((start, stop, text.split('\n')))


class LocalParser(Parser, LocalRecognizer):
    def __init__(self, input, state=None):
	Parser.__init__(self, input, state=state)
	self.setComments([])


class LocalLexer(Lexer, LocalRecognizer):
    renameIdents = kwlist + ['None', 'str', ]

    def __init__(self, input=None, state=None):
	Lexer.__init__(self, input, state)
	self.setComments([])

    def transform(self, node):
	title = tokens.title(tokens.map.get(node.token.type, ''))
	if title:
	    call = getattr(self, 'transform{0}'.format(title), lambda n:None)
	    call(node)

    def transformFalse(self, node):
	node.token.text = node.token.text.title()

    def transformTrue(self, node):
	node.token.text = node.token.text.title()

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

    def transformNull(self, node):
	node.token.text = 'None'


class LocalTree(CommonTree):
    colorTypeMap = {
	'CLASS'            : colortools.green,
	'JAVA_SOURCE'      : colortools.green,
	'VOID_METHOD_DECL' : colortools.green,
	'IDENT'            : colortools.red,
	'TYPE'             : colortools.magenta,
	'EXPR'             : colortools.cyan,
	'TRUE'             : colortools.yellow,
	'FALSE'            : colortools.yellow,
	'NULL'             : colortools.yellow,
    }

    def colorType(self, tokenType):
	return self.colorTypeMap.get(tokenType, colortools.white)(tokenType)

    def colorText(self, tokenType, tokenText):
	return self.colorTypeMap.get(tokenType, colortools.white)(tokenText)

    def colorComments(self, comments):
	text = ''.join(token.text.replace('\n', '') for token in comments)
	return colortools.black(text)

    def dump(self, fd, level=0):
	hasExtra = lambda x, y:x and (x != y)
	comMemo, comTypes = set(), tokens.commentTypes
	nodeFormat = '{0}{1}{2}{3}{4}'

	def innerDump(root, offset):
	    token, indent = root.getToken(), '    ' * offset
	    start, stop = root.getTokenStartIndex(), root.getTokenStopIndex()
	    rng, typ = '', tokens.map.get(token.type, '?')
	    if start and stop and start == stop:
		rng = ' [{0}]'.format(start)
	    elif start and stop:
	        rng = ' [{0}:{1}]'.format(start, stop)
	    args = [indent, self.colorType(typ), '', rng, '']
	    if hasExtra(token.text, typ):
		args[2] = ' ' + self.colorText(typ, token.text)
	    coms = self.selectComments(start, comMemo, comTypes)
	    if coms:
		args[4] = ' ' + self.colorComments(coms)
	    print >> fd, nodeFormat.format(*args)
	    for child in root.getChildren():
		innerDump(child, offset+1)
	innerDump(self, level)

    def selectComments(self, stop, memo, types):
	tokens = self.parser.input.tokens[0:stop]
	tokens = [t for t in tokens if t.type in types and t.index not in memo]
	memo.update(t.index for t in tokens)
	return tokens


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
