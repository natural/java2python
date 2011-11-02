##
# This is an example of how to perform per-module configuration
# for translating java interfaces to zope interfaces.
#
from java2python.mod import basic
from java2python.config import default


# the j2py default head handlers for interfaces includes ABCMeta as a
# metaclass.  we certainly don't want that, so we redefine the list
# here to only the doc string handler:
interfaceHeadHandlers = [
    basic.simpleDocString,
]


# this j2py default is also not what we want, so we redefine it:
methodPrologueHandlers = [
    basic.maybeClassMethod,
]


# instead of the default bases, this handler supplies the base zope
# Interface class for Java interfaces:
interfaceBaseHandlers = [
    basic.zopeInterfaceBases,
]


# the parser adds implemented interfaces to the class bases list.
# this handler checks to see if any of those bases are interfaces, and
# if so, supresses them in favor of 'object' as the only base:
classBaseHandlers = [
    basic.zopeImplementsClassBases,
]


# this handler adds a line like "zope.interface.implements(IFoo)" for
# each interface implemented by a Java class:
classHeadHandlers = [
    basic.zopeImplementsClassHead,
]


# this handler supresses the "self" parameter on method signatures for
# zope Interface definitions:
methodParamHandlers = [
    basic.zopeInterfaceMethodParams,
]
