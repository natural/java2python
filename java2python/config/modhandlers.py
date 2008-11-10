#!/usr/bin/env python
# -*- coding: utf-8 -*-
from java2python.sourcetypes.block import maybeattr


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
        cls = mod.findMainClass()
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
