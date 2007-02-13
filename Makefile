.PHONY: all clean lib


all: lib


clean:
	rm -f *.pyo
	rm -f *.pyc
	cd lib && $(MAKE) clean

lib:
	cd lib && $(MAKE)
