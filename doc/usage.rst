.. _usage:

*****
Usage
*****

Basic Invocation
================

The simplest way to invoke |j2py| is with the :command:`j2py` command
and the name of an input file::

    $ j2py SourceFile.java

The input file may also be specified with the :option:`-i` (or :option:`--input`) option.

The generated source code will be written to ``stdout`` by default.
It can be redirected via the shell or by specifying the :option:`-o`
(or :option:`--output`) option and a filename.

If no input filename is given (or if the input filename is ``-``),
:command:`j2py` reads from ``stdin``.


Options and Arguments
=====================

The :command:`j2py` command accepts options that alter its behavior.
The behavior of the code generator is not part of the command itself;
to change code generation behavior, refer to the :ref:`customization`
chapter.


Code generation:

  * .. option:: -i NAME, --input NAME

    Read from the given file.  Specify ``-`` for ``stdin``.  If not
    given the command will read from ``stdin``.

  * .. option:: -o NAME, --output NAME

    Write to the given file.  Specify ``-`` for ``stdout``.  If not
    given the command will write to ``stdout``.

  * .. option:: -l LEVEL, --loglevel LEVEL

    Set the logging package to the specified log level.  The log level
    may given as an integer (e.g., ``50`` for critical) or by name
    (e.g., ``CRTICIAL``, ``Critical``, or ``critical``).

  * .. option:: -c NAME, --config NAME

    Use the specified configuration module or file.  This option may
    be repeated.

    Configuration modules/files are referenced in reverse order, i.e.,
    from the final value given to the first given, with the default
    configuration referenced last.

    See the :ref:`customization` chapter for details of the
    configuration system and available configuration points.

  * .. option:: -d DIR, --configdir DIR

    Use the given directory name to match input filenames to
    configuration filenames.  For example, to translate
    ``FooBar.java`` and use the configuration stored in
    ``./cfg/FooBar.py``, specify ``-d ./cfg``.

  * .. option:: -n, --nodefaults

    Ignore the default configuration module.

  * .. option:: -r, --nocolor

    Disable colorized output.

    This option has no effect on Windows systems because colorized
    output is always disabled in those environments.

Development:

  * .. option:: -p, --python-tree

    Print a representation of the internal Python code tree.
    Representation is written to ``stderr``.

  * .. option:: -j, --java-ast

    Print a representation of the Java abstract syntax tree.
    Representation is written to ``stderr``.

  * .. option:: -f, --profile

    Profile execution and print the results to ``stederr``.

  * .. option:: -s, --skip-source

    Do not write generated source.  This most useful in development of
    |j2py| itself and when combined with :option:`-p` and/or
    :option:`-j`.


Meta:

  * .. option:: -h, --help

    Show a help message and exit

  * .. option:: --version

    Show the program version number and exit.


