#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import dropwhile
from operator import not_


def ev(left='', right='', format='', **kwds):
    """ Sugar for creating a formatting value dictionary.

    """
    d = dict(left=left, right=right, format=format, )
    d.update(kwds)
    return d


def maybeattr(obj, name, default=None):
    """ Returns named attribute or default.

    """
    return getattr(obj, name, default)


def trimlines(lines):
    """ Removes empty lines from the end of given sequence.

    @return lines without trailing empty lines
    """
    return list(reversed(list(dropwhile(not_, reversed(lines)))))

