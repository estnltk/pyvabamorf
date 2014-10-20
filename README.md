PyVabamorf
==========

PyVabamorf is a Python interface for the Vabamorf Estonian lemmatizer and morphological analyzer.
Vabamorf is a open source morphological analyzer by Filosoft, which can be obtained from here: https://github.com/Filosoft/vabamorf .

# Example

TODO

# Installation

## Windows

Windows users can download pre-built binaries for latest pyvabamorf release:

TODO

## Linux

There are no pre-built binaries for Linux. For building, you need to have installed Python development files (headers and libraries), GCC C++ compiler and also SWIG wrapper generator ( http://swig.org/ ). Depending on your distribution, you might be able to simply install them from software repositories of your distribution.

After all dependencies are installed, the easiest way to build the `pyvabamorf` package is using the pip tool:
```
sudo pip install pyvabamorf
```

Another way is to clone the repository and execute the `setup.py` script inside:
```
sudo python setup.py install
```

Then run the tests and see if they all pass (NB! Don't run them from same directory you have cloned the source distribution):
```
python -m unittest discover pyvabamorf.test
```

# License

Pyvabamorf is licensed under LGPL. See LICENSE for details.
Copyright (c) by Filosoft OÜ and University of Tartu.
