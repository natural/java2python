.. _intro:

************
Introduction
************

What it Does
============

|j2py| reads the Java source files you give it and produces
somewhat-roughly-equivalent Python source code.  It tries to make the
same decisions you would if you were porting the code manually.  It
can perform the translation faster and more accurately than you could,
because it's a dumb machine that does what its told and you're a smart
person with lots of books you haven't read and a love of chocolate so
sometimes you're easily distracted and make mistakes.  Like me and
this documentation.

Where It's Useful
=================

|j2py| can help in two situations.  First, if you're doing a one-time
port of a Java project to Python, it can save you a lot of time and
effort by getting you really far really fast.

Second, if you've got a Java project and you'd like to generate a
Python port and keep the port up to date, you'll find that |j2py| can
help tremendously.  The per-project and per-file configuration system
helps out a lot in this area.

Where |j2py| is not useful is also important.  It won't be useful to
you if you expect your newly translated Python code to run correctly
the first time.  The platforms are too different and this tool is too
limited for that to happen.  Also, you won't find |j2py| very useful
if you expect to convert Java sources at runtime, but that's really a
special case of the former.


How it Works
=============

|j2py| first converts the source code you give it into an abstract
syntax tree.  (That's a lie, really.  |j2py| doesn't do this step,
ANTLR does this step, and ANTLR is a whole lot bigger and cooler than
|j2py| could ever be.  Obviously, really smart people worked on ANTLR
and only one fairly dim one worked on |j2py|).

After the syntax tree is constructed, it's walked and its nodes are
converted to their Python equivalents.  When the walking is complete,
|j2py| takes a few more swipes at it and prints it out.  It's all very
boring, like geology or watching someone learn to play the flute.

This is all well and good for most cases where there exists a very
similar Python construct for the given Java construct.  Classes, for
example, are pretty much the same in both languages.  The trouble
spots are places where a construct exists in Java that is not readily
available in Python.

Note: yes, of course, we're dealing with Turing Machines and they're
equivalent.  If it works in Java, it can work in Python, and I'm not
saying that it can't.  But what I am saying is that there are chunks
of Java source code that you can't make into nice and neat and obvious
Python equivalents.

To get around these trouble spots, |j2py| takes one of two approaches
(and sometimes both if she's feeling especially feisty or if you
haven't paid her much attention lately).  The first approach is to try
and make the problem go away.  For example, in Java the `if` statement
can contain an assignment expression::

    if (++x == 0) { ... }

There isn't a single statement equivalent in Python because assignments
are statements there, not expressions.  So |j2py| does what it can,
presumably what you would do::

    x += 1
    if x == 0:
        ...

Careful readers will have spotted just how close we came to driving
over a cliff with that `++x` expression.  If the increment had been
done on the other side of the variable, the meaning of the statement
would have changed and the Python code would have been wrong.
Fortunately, I've driven by lots of cliffs and have been scared by all
of them so I thought of this ahead of time and decided to do something
about it::

    if (x++ ==0) { ... }

will get translated to::

    mangled_name_for_x = x
    x += 1
    if mangled_name_for_x == 0:
        ...

See what |j2py| did there?  It tried to do what you would do.  For
further explanation and enumeration see the :ref:`features` chapter.


Why Bother?
===========

I bothered to write this because I needed a Java package to run on the
CPython interpreter.  I got tired of porting by hand, so I wrote this
instead.  And it's an interesting problem (kind of).
