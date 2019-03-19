#!/usr/bin/env python

from threading import RLock

_locks = {}
def lock_for_object(obj, locks=_locks):
    return locks.setdefault(id(obj), RLock())

def synchronized(call):
    def inner(*args, **kwds):
        with lock_for_object(call):
            return call(*args, **kwds)
    return inner

class Main(object):

    def __init__(self):
        self.attr = object()

    def b1(self):
        r = []
        with lock_for_object(self.attr):
            r.append(0)
        return r

    def b2(self):
        r = []
        with lock_for_object(self.attr):
            r.append(0)
        return r

    def m1(self):
        return id(lock_for_object(self))

    def m2(self):
        return id(lock_for_object(self))

    @classmethod
    def c1(cls):
        return id(lock_for_object(cls))

    @classmethod
    def c2(cls):
        return id(lock_for_object(cls))

    @synchronized
    def s1(self, *values, **kwargs):
        return [values, kwargs]

    @synchronized
    def s2(self, *values, **kwargs):
        return [values, kwargs]

    @classmethod
    @synchronized
    def cs1(cls, *values, **kwargs):
        return [cls, values, kwargs]

    @classmethod
    @synchronized
    def cs2(cls, *values, **kwargs):
        return [cls, values, kwargs]



if __name__ == '__main__':
    x = Main()
    expected_count = 0

    assert x.b1() == x.b2()
    expected_count += 1 # one for the attr, used twice

    assert x.c1() == x.c2()
    expected_count += 1 # one for the class, used twice

    assert x.m1() == x.m2()
    expected_count += 1 # one for the instance, used twice

    assert x.s1() == x.s2()
    expected_count += 2 # one for each instance method

    assert x.cs1() == x.cs2()
    expected_count += 2 # one for each class method

    assert expected_count == len(_locks)

    print('[PASS]')

