#!/usr/bin/env python
# -*- coding: utf-8 -*-


class FS(object):
    """ Format string abbreviations.

    """
    l = '{left}'
    r = '{right}'
    c = ':'
    lc = l + c
    lr = l + r
    lsr = l + ' ' + r
    lsrc = lsr + c

    @classmethod
    def op(cls, op):
        """ Returns a format string for the given operation.

        """
        l, r = cls.l, cls.r
	if op == '>>>':
	    return '(' + l + ' & (2**32+' + l + ')) >> ' + r
	if op == '>>>=':
	    return l + ' = bsr(' + l + ', ' + r + ')'
	return l + ' ' + op + ' ' + r
