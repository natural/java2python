PYTHONPATH=..
CLASSPATH=.

java_sources := $(wildcard *.java)
py_sources := $(addsuffix .py, $(notdir $(basename $(wildcard *.java))))


.SILENT: clean
.PHONY: all $(java_sources) $(python_sources) clean X

all: $(java_sources)


$(java_sources):
	javac $@  && ../java2python/bin/j2py -i $@ -o $(basename $@).py -c testconfig
	@chmod u+x $(basename $@).py
	@bash ./compare_outputs.sh "java -ea $(basename $@)" "python $(basename $@).py" "$@"


%.py: %.java testconfig.py
	../java2python/bin/j2py -i $< -o $@ -c testconfig
	python $@

%: %.java
	javac $<
	java $@

clean:
	rm -f *.class *.pyc $(py_sources)
