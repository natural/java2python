#!/usr/bin/env python
# -*- coding: utf-8 -*-
from logging import warn
from java2python import maybeAttr


def insertPreamble(module, output):
    module.dumpConfigValues(output, 'modulePreamble')


def insertEpilogue(module, output):
    module.dumpConfigValues(output, 'moduleEpilogue')


def findMainClass(module):
    """ Given a list of source objects, locate a class name that
        matches the block.
    """
    lines = module.lines
    try:
        classes = [c for c in lines if maybeAttr(c, 'name')==module.name]
        if classes:
            cls = classes[0]
        else:
            cls = [c for c in lines if maybeAttr(c, 'isClass')][0]
    except (IndexError, ):
        cls = None
    return cls


def ifMainScript(module, output):
    """ writes a block to call the module as a script

    @param output writable file-like object
    @return None
    """
    try:
        cls = findMainClass(module)
        methods = [m for m in cls.lines if maybeAttr(m, 'isMethod')]
        main = [m for m in methods if m.name == 'main'][0]
    except (AttributeError, IndexError, ):
        pass
    else:
        if main.isStatic and main.isPublic and main.isVoid:
            name = cls.name
            offset = module.offset(1)
            output.write("\n\nif __name__ == '__main__':\n")
            output.write("%simport sys\n" % offset)
            output.write("%s%s.main(sys.argv)\n" % (offset, name))
