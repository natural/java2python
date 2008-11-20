#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import cmd

from antlr3 import ANTLRStringStream
from antlr3.tree import CommonTreeNodeStream

from java2python.blocks import Module
from java2python.parser.local import LocalTokenStream
from java2python.parser.JavaParser import JavaParser
from java2python.parser.JavaLexer import JavaLexer
from java2python.parser.JavaTreeParser import JavaTreeParser


def sourceObjects(source):
    stream = ANTLRStringStream(source)
    lexer = JavaLexer(stream)
    tokens = LocalTokenStream(lexer)
    parser = JavaParser(tokens)
    root = parser.javaSource().tree
    nodes = CommonTreeNodeStream(root)
    nodes.setTokenStream(tokens)
    walker = JavaTreeParser(nodes)
    return stream, lexer, tokens, parser, walker


class ExprShell(cmd.Cmd):
    prompt = ": "

    def __init__(self, completekey='tab', stdin=None, stdout=None, options=None,
                 version=None):
        cmd.Cmd.__init__(self, completekey, stdin, stdout)
        intro = "java2python expression evaluator version %s (rNNN, date)\n" % (version, )
        intro += "%s on %s\n" % (sys.version.split('\n')[1], sys.platform, )
        intro += 'Type "help", "copyright" or "license" for more information.'
        self.intro = intro
        self.options = options

    def do_expr(self, line):
        line = line.strip()
        if not line:
            return
        if not line.startswith(('class ', 'interface ', 'enum ', 'annotation ')):
            line = "class internal { %s }" % (line, )
            def locate(b):
                for i in b.lines[0]:
                    if isinstance(i, (dict, )):
                        i = b.formatExpression(i)
                    return i
        else:
            def locate(b):
                return b
        try:
            stream, lexer, tokens, parser, walker = sourceObjects(line)
            mod = Module('<interactive>', '<interactive>')
            mod.setConfigs(self.options.configs)
            walker.javaSource(mod)
            out = locate(mod)
            try:
                out = out.asString()
            except (AttributeError, ):
                out += '\n'
        except (Exception, ), exc:
            self.stdout.write('Exception during transform: %s\n' % (exc.args[0], ))
        else:
            self.stdout.write(out)

    def do_copyright(self, line):
        self.stdout.write("Copyright 2008 Troy Melhase <troy@gci.net>\n")

    def do_license(self, line):
        self.stdout.write("GPL2.  See LICENSE file for full license text.\n")

    def do_method(self, meth):
        pass

    def do_statement(self, stat):
        pass

    def do_EOF(self, other):
        self.stdout.write('\n')
        return True

    def do_quit(self, other):
        return True
    do_q = do_quit

    def emptyline(self):
        pass

    def default(self, line):
        self.stdout.write("* Unknown command: %s\n" % (line, ))
