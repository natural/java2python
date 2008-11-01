#!/usr/bin/env python
# -*- coding: utf-8 -*-
from java2python.sourcetypes.block import Block, maybeAttr


class Module(Block):
    """ Module -> specialized block type

    Module instances write a preamble before writing their source
    objects.  They write an epilogue as well, and are responsible for
    writing a "if __name__ == '__main__'" block.
    """
    def __init__(self, infile, outfile):
        baseout = outfile.split('.py')[0]
        basein = infile.split('.java')[0]
        name = (baseout if baseout and baseout != '-' else basein)
        Block.__init__(self, parent=None, name=name)
        self.infile = infile
        self.outfile = outfile

    def dump(self, output, indent):
        """ writes the string representation of this block

        @param output any writable file-like object
        @param indent indentation level of this block
        @return None
        """
        self.dumpConfigValues(output, 'modulePreamble')
        Block.dump(self, output, indent)
        self.dumpConfigValues(output, 'moduleEpilogue')
        self.dumpIfMainScript(output)

    def dumpConfigValues(self, output, name):
        """ writes a sequence of lines given a config attribute name

        Lines may be callable.  Refer to the config.default module for
        details.

        @param output writable file-like object
        @param name configuration module attribute
        @return None
        """
        for lines in self.config.all(name, []):
            for line in lines:
                line = line(self) if callable(line) else line
                output.write('%s\n' % (line, ))

    def dumpIfMainScript(self, output):
        """ writes a block to call the module as a script

        @param output writable file-like object
        @return None
        """
        if not self.config.last('writeMainMethodScript'):
            return
        try:
            cls = self.findMainClass()
            methods = [m for m in cls.lines if maybeAttr(m, 'isMethod')]
            main = [m for m in methods if m.name == 'main'][0]
        except (AttributeError, IndexError, ):
            pass
        else:
            mods = main.modifiers
            typ = main.type
            if ('public' in mods) and ('static' in mods) and (typ in ('void', None)):
                name = cls.name
                offset = self.I(1)
                output.write("if __name__ == '__main__':\n")
                output.write("%simport sys\n" % offset)
                output.write("%s%s.main(sys.argv)\n" % (offset, name))

    def findMainClass(self):
        try:
            clss = [c for c in self.lines if maybeAttr(c, 'name')==self.name]
            if clss:
                cls = clss[0]
            else:
                cls = [c for c in self.lines if maybeAttr(c, 'isClass')][0]
        except (IndexError, ):
            cls = None
        return cls

