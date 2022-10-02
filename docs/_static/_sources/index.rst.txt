.. Args Enum documentation master file, created by
   sphinx-quickstart on Sun Oct  2 06:42:01 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Args Enum
=========

Use the standard ``enum.Enum`` class to organize your program's CLI parameters.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Quick Start
===========

Create groups of arguments as ``Enum`` classes, and single options
as instances of the provided ``Actions`` class:

    | ``Parser(*Group(s), **Actions) -> ArgumentParser``

A minimal example::

    import args_enum as aenm

    AppParser = aenm.Parser(
        aenm.Log,
        QUIET = aenm.Flag.TRUE("log level 'WARNING'"),
        DEBUG = aenm.Flag.TRUE("log level 'DEBUG'")
    )
    args = AppParser.parse_args()

The code above will produce the following ``--help`` output::

    usage: your_program.py [-h] [--quiet] [--debug]
                [--log-level {NOTSET,TRACE,DEBUG,INFO,WARNING}]
                [--log-dir LOG_DIR]

    options:
    -h, --help            show this help message and exit
    --quiet               log level 'WARNING'
    --debug               log level 'DEBUG'

    log:
    --log-level {NOTSET,TRACE,DEBUG,INFO,WARNING}
                            Program logger output verbosity
    --log-dir LOG_DIR     Destination directory for log files


New groups are created by sub-classing ``Group``::

    class Py(Group):
        VERSION = Flag.TRUE()

The above code will produce a group called ``py`` and
exposes the option ``--py-version`` in the command line.
To retrieve the value in your program, access the
``PY_VERSION`` member of the relevant Namespace.

