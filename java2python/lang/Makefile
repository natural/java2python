.PHONY: all clean
.SILENT: clean

all: JavaParser.py JavaLexer.py SelectorParser.py SelectorLexer.py


JavaParser.py: Java.g
	antlr3 Java.g


JavaLexer.py: Java.g
	antlr3 Java.g


SelectorParser.py: Selector.g
	antlr3 Selector.g

SelectorLexer.py: Selector.g
	antlr3 Selector.g


clean:
	rm -f *.pyo
	rm -f *.pyc
	rm -f *Parser.py
	rm -f *Lexer.py
	rm -f *.tokens




