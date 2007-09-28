PYTHONPATH=../../:.
CLASSPATH:=.:/usr/share/junit/lib/junit.jar

PYOBJS=AssignInExpr.py EmptyArray.py
JAVAOBJS=AssignInExpr EmptyArray

all: python-test

python-test: $(PYOBJS)

java-test: $(JAVAOBJS)

%.py: %.java testconfig.py
	../bin/j2py -i $< -o $@ -c testconfig
	python $@

%: %.java
	javac $<
	java junit.textui.TestRunner $@

clean:
	rm -f $(PYOBJS)
	rm -f *.class *.pyc
