#!/usr/bin/env python
from antlr3 import CommonTokenStream
from antlr3.tree import CommonTreeAdaptor


class CommentSavingCommonTreeAdaptor(CommonTreeAdaptor):
    def createWithPayload(self, *args):
	tok = CommonTreeAdaptor.createWithPayload(self, *args)
        val = args[0] if args else None
        tok.comment = getattr(val, 'comment', None)
        return tok


class LocalTokenStream(CommonTokenStream):
    def skipOffTokenChannels(self, i):
        j = i
        try:
            while self.tokens[i].channel != self.channel:
                i += 1
        except (IndexError, ):
            pass
        vals = [(t.getType(), t.getText()) for t in self.tokens[j:i]]
        vals = [(typ, txt) for typ, txt in vals if txt.strip()]
        if vals:
            k = i
            try:
                while self.tokens[k].channel != self.channel:
                    k += 1
            except (IndexError, ):
                pass
            self.tokens[k].comment = vals
        return i
