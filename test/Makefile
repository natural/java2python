javac := javac
java := java
python := python -B
j2py = ../bin/j2py


python_files := $(addsuffix .py, $(notdir $(basename $(wildcard *.java))))
test_targets := $(sort $(notdir $(basename $(wildcard *.java))))

export PYTHONPATH := $(PYTHONPATH):.:..


.PHONY: all clean
.SILENT: %:


all:
	$(MAKE) $(test_targets)


selectors:
	@cd selector && make


clean:
	@rm -f *.class *.pyc $(python_files)


packages:
	@cd Package0 && javac Class0.java
	@cd Package0 && ../$(j2py) Class0.java Class0.py


parsers:
	@cd ../java2python/lang && make -s


%.class:
	[ -s $(addsuffix .java, $(basename $@)) ] && $(javac) $(addsuffix .java, $(basename $@))


%.py: %.class
	@$(j2py) $(addsuffix .java, $(basename $@)) $@ -c configs.defaults -d configs

%: %.py
	@bash -c "diff -u <($(python) $(addsuffix .py, $@)) <(java -ea $@)" && echo "[PASS] $@"
