.PHONY: all clean parser


all: parser


clean:
	rm -f *.pyo
	rm -f *.pyc
	cd parser && $(MAKE) clean

parser:
	cd parser && $(MAKE)
