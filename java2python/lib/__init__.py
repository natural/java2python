#!/usr/bin/env python
# -*- coding: utf-8 -*-


class FS(object):
    l = '{left}'
    r = '{right}'
    c = ':'
    lc = l + c
    lr = l + r
    lsr = l + ' ' + r
    lsrc = lsr + c

    #instance = 'isinstance(' + l + ', (' + t + ', ))'
    @classmethod
    def op(cls, op):
	if op == '>>>':
	    return '({left} & (2**32+{left})) >> {right}'
	if op == '>>>=':
	    return '{left} = bsr({left}, {right})'
	return cls.l + ' ' + op + ' ' + cls.r
