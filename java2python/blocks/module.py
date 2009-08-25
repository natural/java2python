#!/usr/bin/env python
# -*- coding: utf-8 -*-
from logging import warn
from java2python.blocks.block import Block


class Module(Block):
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
            for writer in self.config.handlers(key):
                writer(self, output)

        doWriters('modulePreambleWriters')
        for line in self.preamble:
            output.write('\n%s' % line)
        Block.dump(self, output, indent)
        doWriters('moduleEpilogueWriters')
