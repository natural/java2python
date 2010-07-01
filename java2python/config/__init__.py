#!/usr/bin/env python
# -*- coding: utf-8 -*-
from java2python.lib import getModule, getModuleValue


def valueOf(item):
    return getModuleValue(item) if isinstance(item, (basestring, )) else item


class Config(object):
    """ Config -> wraps multiple configuration modules

    """
    def __init__(self, names):
	self.configs = [getModule(name) for name in names]

    def __iter__(self):
	return iter(self.configs)

    def every(self, key, default=None):
	return [getattr(config, key, default) for config in self]

    def last(self, key, default=None):
	for config in reversed(list(self)):
	    if hasattr(config, key):
		return getattr(config, key)
	return default

    def combined(self, key):
	combined = {}
	for mapping in self.every(key, {}):
	    combined.update(mapping)
	return combined

    def handler(self, key, default=None):
	handler = self.last(key, default)
	return valueOf(handler) if handler is not default else handler

    def handlers(self, key, default=None):
	groups = self.every(key, default)
	if groups is not default:
	    for group in groups:
		for handler in group:
		    yield valueOf(handler)
