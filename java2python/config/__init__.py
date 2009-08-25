#!/usr/bin/env python
# -*- coding: utf-8 -*-
from java2python import importModule, maybeImport


class Config:
    """ Config -> wraps multiple configuration modules

    """
    def __init__(self, names):
        self.configs = [importModule(name) for name in names]

    def all(self, name, missing=None):
        """ value of name in each config module

        @param name module attribute as string
        @keyparam missing=None default for missing attributes
        @return sequence of values
        """
        return (getattr(config, name, missing) for config in self.configs)

    def last(self, name, default=None):
        """ value from final config module to define name

        @param name module attribute as string
        @keyparam default=None value returned if all modules lack name
        @return value from config module
        """
        for config in reversed(self.configs):
            if hasattr(config, name):
                return getattr(config, name)
        return default

    def combined(self, name):
        """ combined mapping of named dictionaries from all config modules

        @param name attribute as string
        @return dictionary updated with each named dictionary
        """
        combined = {}
        for mapping in self.all(name, {}):
            combined.update(mapping)
        return combined

    def handler(self, name, default=None):
        """ single handler from last config module, possibly imported

        @param name handler attribute as string
        @keyparam default=None value returned if all modules lack name
        @return value from config module
        """
        item = self.last(name, default)
        if item is not default:
            item = maybeImport(item)
        return item

    def handlers(self, name):
        """ yields handlers from last config module, each possibly imported

        @param name handler attribute as string
        @return list of values
        """
        handlers = self.last(name, ())
        for handler in handlers:
            yield maybeImport(handler)
