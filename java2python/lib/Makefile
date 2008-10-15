.PHONY: all clean


all: parser.py lexer.py walker.py


lexer.py: java15.g
	runantlr java15.g


parser.py: java15.g
	runantlr java15.g


walker.py: walker.g
	runantlr walker.g


clean:
	rm -f *.pyo
	rm -f *.pyc
	rm -rf lexer.py
	rm -rf parser.py
	rm -rf walker.py
	rm -rf walkerTokenTypes.txt
	rm -rf JavaTokenTypes.txt
