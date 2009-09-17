#!/usr/bin/env python
# -*- coding: utf-8 -*-





class Annotation(object):
    """ An example Annotations base class.

    """
    registry = {}

    def __init__(self, **kwds):
        self.kwds = kwds

    def __call__(self, obj):
        annotations = self.registry.setdefault(self.__class__.__name__, {})
        annotations[obj] = self.kwds
        return obj


class Enum(object):
    pass
