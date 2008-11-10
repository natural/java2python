#!/usr/bin/env python
# -*- coding: utf-8 -*-
from java2python import maybeattr


def preamble(mod, output):
    mod.dumpConfigValues(output, 'modulePreamble')


def epilogue(mod, output):
    mod.dumpConfigValues(output, 'moduleEpilogue')


def ifMainScript(mod, output):
    """ writes a block to call the module as a script

    @param output writable file-like object
    @return None
    """
    try:
        cls = findMainClass(mod)
        methods = [m for m in cls.lines if maybeattr(m, 'isMethod')]
        main = [m for m in methods if m.name == 'main'][0]
    except (AttributeError, IndexError, ):
        pass
    else:
        mods = main.modifiers
        typ = main.type
        if ('public' in mods) and ('static' in mods) and (typ in ('void', None)):
            name = cls.name
            offset = mod.I(1)
            output.write("if __name__ == '__main__':\n")
            output.write("%simport sys\n" % offset)
            output.write("%s%s.main(sys.argv)\n" % (offset, name))


def findMainClass(mod):
    """ Given a list of source objects, locate a class name that matches the block.

    """
    try:
        clss = [c for c in mod.lines if maybeattr(c, 'name')==mod.name]
        if clss:
            cls = clss[0]
        else:
            cls = [c for c in mod.lines if maybeattr(c, 'isClass')][0]
    except (IndexError, ):
        cls = None
    return cls

