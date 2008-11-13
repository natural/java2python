#!/usr/bin/env python
# -*- coding: utf-8 -*-
from java2python import maybeimport
from java2python.sourcetypes.block import Block


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
        def doWriters(key):
            for writer in self.config.last(key, ()):
                writer = maybeimport(writer)
                writer(self, output)
        doWriters('modulePreambleWriters')
        Block.dump(self, output, indent)
        doWriters('moduleEpilogueWriters')
