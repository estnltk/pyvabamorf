PyVabamorf
==========

PyVabamorf is a Python interface for the Vabamorf Estonian lemmatizer and morphological analyzer.
Vabamorf is a open source version of _estmorf_ morphological analyzer by Filosoft, which can be obtained from here: https://github.com/Filosoft/vabamorf .

# License

Pyvabamorf is licensed under LGPL. See LICENSE for details.
Copyright (c) by Filosoft OÜ and University of Tartu.

# Prerequisites

In able to build the package, you need to have configured necessary development tools on your system. Refer to documentation of _distutils_ to see, how this should be done. But you are already good to go, if for example you have  installed _numpy_ or _scipy_ packages from source previously using _distutils_.
In a nutshell, you need following:
- C++ compiler
- Python development libraries
- Another dependency required by PyVabamorf is SWIG wrapper generator that can be downloaded from http://swig.org/ .

# Installation

To build and install the Python library on Linux, invoke the following commands:
```
python setup.py build
sudo python setup.py install
```

Then run the tests and see if they all pass:
```
python -m unittest discover pyvabamorf.test
```

PyVabamorf should work with both Python 2.x and Python 3.x versions, although we have tested it currently only with Python 2.7 and Python 3.3.

## Binary packages

We plan to release precompiled and easily installable packages for both 32 and 64 bit versions of Linux and Windows.

# Usage examples

todo

