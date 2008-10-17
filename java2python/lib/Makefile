.PHONY: all clean


all: JavaParser.py JavaLexer.py JavaTreeParser.py


JavaParser.py: Java.g
	antlr3 Java.g


JavaLexer.py: Java.g
	antlr3 Java.g

# JavaLexer.py


JavaTreeParser.py: JavaTreeParser.g 
	antlr3 JavaTreeParser.g


clean:
	rm -f *.pyo
	rm -f *.pyc
	rm -rf JavaParser.py
	rm -rf JavaLexer.py
	rm -rf JavaTreeParser.py
	rm -rf Java.tokens
	rm -rf JavaTreeParser.tokens

