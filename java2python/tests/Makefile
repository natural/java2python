PYTHONPATH=../../:.
CLASSPATH=/usr/share/java/junit.jar:.

java_sources := $(wildcard *.java)
py_sources := $(addsuffix .py, $(notdir $(basename $(wildcard *.java))))

.SILENT: clean
.PHONY: all $(java_sources) $(python_sources) clean

all: $(java_sources)


$(java_sources):
	javac $@  && ../bin/j2py -i $@ -o $(basename $@).py -c testconfig
	@chmod u+x $(basename $@).py
	@bash ./compare_outputs.sh "java $(basename $@)" "python $(basename $@).py" "$@"

java-test: $(JAVAOBJS)

%.py: %.java testconfig.py
	../bin/j2py -i $< -o $@ -c testconfig
	python $@

%: %.java
	javac $<
	java junit.textui.TestRunner $@

clean:
	rm -f *.class *.pyc $(py_sources)
