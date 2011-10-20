.PHONY: all

test_targets := $(sort $(notdir $(basename $(wildcard *.py))))


all:
	$(MAKE) $(test_targets)

%:
	@python -m unittest -v $@


