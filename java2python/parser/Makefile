.PHONY: all clean
.SILENT: clean

all: JavaParser.py # JavaTreeParser.py


JavaParser.py: Java.g
	antlr3 Java.g


JavaLexer.py: Java.g
	antlr3 Java.g


#JavaTreeParser.py: JavaTreeParser.g JavaLexer.py
#	antlr3 JavaTreeParser.g


clean:
	rm -f *.pyo
	rm -f *.pyc
	rm -rf JavaParser.py
	rm -rf JavaLexer.py
	rm -rf JavaTreeParser.py
	rm -rf Java.tokens
	rm -rf JavaTreeParser.tokens
	rm -rf Java__.g
