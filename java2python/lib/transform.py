from antlr3 import CommonTokenStream, ANTLRStringStream

from java2python.blocks import BlockFactory
from java2python.config import Config
from java2python.parser.local import LocalTreeAdaptor
from java2python.parser.JavaLexer import JavaLexer
from java2python.parser.JavaParser import JavaParser


def transform(source, configs):
    lexer = JavaLexer(ANTLRStringStream(source))
    lexer.comments = []
    parser = JavaParser(CommonTokenStream(lexer))
    parser.factory = BlockFactory(Config(configs))
    parser.comments = lexer.comments
    parser.setTreeAdaptor(LocalTreeAdaptor(callback=parser.checkNode))
    module = parser.compilationUnit().module
    return module

