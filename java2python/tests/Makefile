PYTHONPATH=..:.
## CLASSPATH=.

java_sources := $(wildcard *.java)
py_sources := $(addsuffix .py, $(notdir $(basename $(wildcard *.java))))


.SILENT: clean
.PHONY: all $(java_sources) $(python_sources) clean X

all: package_1 $(java_sources)

package_1:
	cd Package1 && ../../bin/j2py -i Class1.java  -o Class1.py

$(java_sources):
	@javac $@  && ../bin/j2py -i $@ -o $(basename $@).py -c testconfig
	@chmod u+x $(basename $@).py
	@bash ./compare_outputs.sh "java -ea $(basename $@)" "python $(basename $@).py" "$@" && rm "$(basename $@).py" "$(basename $@).class"


%.py: %.java testconfig.py
	../bin/j2py -i $< -o $@ -c testconfig
	python $@

%: %.java
	javac $<
	java $@

clean:
	rm -f *.class *.pyc $(py_sources)

parser:
	cd ../parser && make
