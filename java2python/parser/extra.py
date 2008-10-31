#!/usr/bin/env python
from antlr3 import CommonTokenStream
from antlr3.tree import CommonTreeAdaptor, TreeParser

from java2python.parser import JavaLexer
from java2python.sourcetypes import SimplePythonSourceStack


class LocalTreeParser(TreeParser):
    """

    """
    def __init__(self, *a, **b):
	super(LocalTreeParser, self).__init__(*a, **b)
        self.commentHandler = CommentFormatter(self)
        self.source = None

    def onJavaSource(self, module):
        self.source = SimplePythonSourceStack(module)

    def __getattr__(self, name):
        return getattr(self.source, name)


class LocalTreeAdaptor(CommonTreeAdaptor):
    """ Replacement tree adapter that copies comment sequences from
        lexer tokens to tree tokens.

        Check the Java.g grammar file to see how this class is used.
    """
    def createWithPayload(self, payload):
	token = super(LocalTreeAdaptor, self).createWithPayload(payload)
        token.comments = getattr(payload, 'comments', None)
        return token


class LocalTokenStream(CommonTokenStream):
    """ Token stream subclass that saves comment sequences in lexed
        tokens.

    """
    commentTargetTypes = [
        JavaLexer.CLASS,
        JavaLexer.IDENT,
    ]

    def skipOffTokenChannels(self, start):
        stop = start
        try:
            while self.tokens[stop].channel != self.channel:
                stop += 1
        except (IndexError, ):
            pass
        self.maybeSaveComments(start, stop)
        return stop

    def maybeSaveComments(self, start, stop):
        vals = [(t.getType(), t.getText()) for t in self.tokens[start:stop]]
        vals = [(typ, txt) for typ, txt in vals if txt.strip()]
        cursor = start
        try:
            ## seek backward to a suitable token
            while self.tokens[cursor].getType() not in self.commentTargetTypes:
                if not cursor: break
                cursor -= 1
        except (IndexError, ):
            pass
        if not cursor:
            cursor = start
            ## no suiltable token found looking backward, seek forward
            ## instead (this happens with comments before initial
            ## declaration in input source)
            while self.tokens[cursor].getType() not in self.commentTargetTypes:
                cursor += 1
        self.reallySaveComments(vals, cursor)


    def reallySaveComments(self, values, cursor):
        try:
            comments = getattr(self.tokens[cursor], 'comments', None)
        except (IndexError, ):
            pass
        else:
            if comments is None:
                self.tokens[cursor].comments = values[:]
            else:
                for comment in values:
                    if comment not in comments:
                        comments.append(comment)


class CommentFormatter(object):
    def __init__(self, parser):
        self.parser = parser
        self.commentFormatters = {
            JavaLexer.COMMENT : self.formatMultiLineComment,
            JavaLexer.LINE_COMMENT : self.formatLineComment,
            }

    def formatMultiLineComment(self, v):
        v = v.strip()[2:-2]
        for line in v.split('\n'):
            line = line.strip()
            if line.startswith('*'):
                line = line[1:]
            if line.endswith('*'):
                line = line[:-1]
            yield line.strip()

    def formatLineComment(self, v):
        yield v[2:].strip()

    def __call__(self, start):
        input, source = self.parser.input, self.parser.source
        start_idx = input.getTreeAdaptor().getTokenStartIndex(start)
        stop_idx = input.getTreeAdaptor().getTokenStopIndex(start)
        tokens = input.tokens.tokens[start_idx:stop_idx]
        comments = [(t, getattr(t, 'comments', None)) for t in tokens]
        comments = [(t, c) for t, c in comments if c]
        for token, comment_set in comments:
            token.comments = None
            for typ, val in comment_set:
                formatter = self.commentFormatters[typ]
                for line in formatter(val):
                    if line:
                        source.current.addComment(line)
