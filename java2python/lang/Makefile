.PHONY: all clean
.SILENT: clean

all: JavaParser.py JavaLexer.py


JavaParser.py: Java.g
	antlr3 Java.g


JavaLexer.py: Java.g
	antlr3 Java.g


clean:
	rm -f *.pyo
	rm -f *.pyc
	rm -rf JavaParser.py
	rm -rf JavaLexer.py
	rm -rf Java.tokens
	rm -rf JavaTreeParser.tokens
	rm -rf Java__.g
