.PHONY: all clean parser
.SILENT: clean


all: parser


clean:
	rm -f *.pyo
	rm -f *.pyc
	cd parser && $(MAKE) clean

parser:
	cd parser && $(MAKE)
