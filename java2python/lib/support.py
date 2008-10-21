from sys import stderr
from os import environ

enable_trace = int(environ.get('J2PYDEBUG', 0))
indents = [0]


def trace_line(v):
    if enable_trace:
        print >> stderr, v


def tracer(call):
    name = call.__name__
    def traced_call(*args, **kwds):
        indent = indents[-1]
        indents.append(indent+1)
        spacer = "    "*indent
        print_args = "%s" % (args[1:], ) if args[1:] else ""
        print >> stderr, "%s%s %s %s" % (spacer, "enter", name, print_args)
        call_value = call(*args, **kwds)
        print_ret = "(result %s)" % (call_value, ) if call_value is not None else ""
        print >> stderr, "%s%s %s %s" % (spacer, "exit", name, print_ret, )
        indents.pop()
        return call_value
    return traced_call if enable_trace else call


