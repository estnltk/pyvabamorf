PyVabamorf
==========

PyVabamorf is a Python interface for the Vabamorf Estonian lemmatizer and morphological analyzer.
Vabamorf is a open source version of _estmorf_ morphological analyzer by Filosoft,
which can be obtained from here: https://github.com/Filosoft/vabamorf .

# License

Pyvabamorf is licensed under LGPL. See LICENSE for details.
Copyright (c) by Filosoft OÜ and University of Tartu.

# Prerequisites

In order to build the package, you need to have configured necessary development tools on your system.
Refer to documentation of _distutils_ to see, how this should be done. But you are already good to go,
if for example you have  installed _numpy_ or _scipy_ packages from source previously using _distutils_.
In a nutshell, you need following:
- C++ compiler
- Python development libraries

Additional dependencies:
- SWIG wrapper generator that can be downloaded from http://swig.org/ . We are currently using version 3.0 on development machines.

# Installation

To build and install the library on Linux, invoke the following commands:
```
python setup.py build
sudo python setup.py install
```

Then run the tests and see if they all pass (NB! Don't run them from same directory you have cloned the source distribution):
```
python -m unittest discover pyvabamorf.test
```

PyVabamorf should work with both Python 2.x and Python 3.x versions, although we have tested it
currently only with Python 2.7 and Python 3.3.

## Binary packages

We plan to release precompiled and easily installable packages for both 32 and 64 bit versions of Linux and Windows.
We also plan to submit the main releases of the package to the Python Package Index (PyPI),
so the library can be installed using the _pip_ tool.

# Usage examples

## Morphological analysis and lemmatization

Python3 code:
```python
from pyvabamorf import PyVabamorf
from pprint import pprint

m = PyVabamorf()
pprint(m.analyze('Tüüne öötöömiljöö allmaaraudteejaamas!'.split()))
```

One thing to note about Vabamorf library, is that it yet does not do morphological disambiguation found in commercial
version of the library. Therefore the output contains all possible analysis variants.

Output:
```
[{'analysis': [{'clitic': '',
                'ending': '0',
                'form': 'sg g',
                'lemma': 'tüün',
                'lemma_tokens': ['tüün'],
                'partofspeech': 'A',
                'root': 't<üün'},
               {'clitic': '',
                'ending': '0',
                'form': 'sg g',
                'lemma': 'tüüne',
                'lemma_tokens': ['tüüne'],
                'partofspeech': 'A',
                'root': 't<üüne'},
               {'clitic': '',
                'ending': '0',
                'form': 'sg n',
                'lemma': 'tüüne',
                'lemma_tokens': ['tüüne'],
                'partofspeech': 'A',
                'root': 't<üüne'}],
  'text': 'Tüüne'},
 {'analysis': [{'clitic': '',
                'ending': '0',
                'form': 'sg g',
                'lemma': 'öötöömiljöö',
                'lemma_tokens': ['öö', 'töö', 'miljöö'],
                'partofspeech': 'S',
                'root': '<öö_t<öö_milj<öö'},
               {'clitic': '',
                'ending': '0',
                'form': 'sg n',
                'lemma': 'öötöömiljöö',
                'lemma_tokens': ['öö', 'töö', 'miljöö'],
                'partofspeech': 'S',
                'root': '<öö_t<öö_milj<öö'}],
  'text': 'öötöömiljöö'},
 {'analysis': [{'clitic': '',
                'ending': 's',
                'form': 'sg in',
                'lemma': 'allmaaraudteejaam',
                'lemma_tokens': ['all', 'maa', 'raud', 'tee', 'jaam'],
                'partofspeech': 'S',
                'root': '<all_m<aa_r<aud_t<ee_j<aam'}],
  'text': 'allmaaraudteejaamas!'}]
```


## Spell-check

TODO

## Generating word forms from root

TODO


