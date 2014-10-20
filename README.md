PyVabamorf
==========

PyVabamorf is a Python interface for the Vabamorf Estonian lemmatizer and morphological analyzer.
Vabamorf is a open source morphological analyzer by Filosoft, which can be obtained from here: https://github.com/Filosoft/vabamorf .

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
- SWIG wrapper generator that can be downloaded from http://swig.org/ . We are currently using version 2.0.10 on development machines.

# Installation

To build and install the library on Linux, invoke the following commands:
```
python setup.py build
sudo python setup.py install
```

Alternatively, you can use _pip_ tool to download and install the library from Python Package Index (PyPI). You still need to install necessary dependencies to build the package.

```
sudo pip install pyvabamorf
```

Then run the tests and see if they all pass (NB! Don't run them from same directory you have cloned the source distribution):
```
python -m unittest discover pyvabamorf.test
```

PyVabamorf works with Python 2.7 and Python 3.4 versions. It might work with other versions as well, but we have not tested this.

A known bug related to multiprocessing in Windows for Python 2.7, that also fails in one of the unit tests:
* http://stackoverflow.com/questions/16405687/python-2-7-on-windows-assert-main-name-not-in-sys-modules-main-name-for-all
* http://bugs.python.org/issue10845

### Windows specifics

In order to build the library with visual studio, you might get an error related to not finding `vcvarsall.bat` file. If you have Visual Studio 2010 installed, execute
```
SET VS90COMNTOOLS=%VS100COMNTOOLS%
```
or with Visual Studio 2012 installed (Visual Studio Version 11)
```
SET VS90COMNTOOLS=%VS110COMNTOOLS%
```
or with Visual Studio 2013 installed (Visual Studio Version 12)
```
SET VS90COMNTOOLS=%VS120COMNTOOLS%
```
See http://stackoverflow.com/questions/2817869/error-unable-to-find-vcvarsall-bat for more details.

## Binary packages

All existing binary packages can be found in `dist` folder of the project. Currently there are:

- pyvabamorf-1.3.win32-py2.7.msi

Note to users: if you manage to build a specific version that does not yet exist, feel free to contribute your installer.

# Usage examples

## Morphological analysis and lemmatization

Python3 code:
```python
from pyvabamorf import analyze_sentence
from pprint import pprint

pprint(analyze_sentence('Tüüne öötöömiljöö allmaaraudteejaamas!'.split()))
```

NB! If you run above in a Windows terminal and it complains about unicode, you can try instead:

```python
from pyvabamorf import analyze_sentence
from pprint import pprint
import sys

pprint(analyze_sentence('Tüüne öötöömiljöö allmaaraudteejaamas!'.decode(sys.stdin.encoding).split()))
```

One thing to note about Vabamorf library, is that it yet does not do morphological disambiguation. Gossips say, it will be added in future. When it is done, there will also be an option to use it.

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

It is possible to use `analyze_sentence` function in `multiprocessing` methods, such as `Pool.map`. This is convenient to speed up processing large corpora.

```
>>> from pyvabamorf import analyze_sentence
>>> from multiprocessing import Pool
>>> from pprint import pprint
>>> 
>>> pool = Pool(2) # pool with two processes
>>> sentences = [u'Tere maailm, mis teoksil?'.split(),
...              u'Täna tuleb imeilus päev!'.split()]
>>> pprint(pool.map(analyze_sentence, sentences))
[[{'analysis': [{'clitic': '',
                 'ending': '0',
                 'form': '',
                 'lemma': 'tere',
                 'lemma_tokens': ['tere'],
                 'partofspeech': 'I',
                 'root': 'tere'},
                {'clitic': '',
                 'ending': '0',
                 'form': 'sg g',
                 'lemma': 'tere',
                 'lemma_tokens': ['tere'],
                 'partofspeech': 'S',
                 'root': 'tere'},
                {'clitic': '',
                 'ending': '0',
                 'form': 'sg n',
                 'lemma': 'tere',
                 'lemma_tokens': ['tere'],
                 'partofspeech': 'S',
                 'root': 'tere'}],
   'text': 'Tere'},
  {'analysis': [{'clitic': '',
                 'ending': '0',
                 'form': 'sg n',
                 'lemma': 'maailm',
                 'lemma_tokens': ['maa', 'ilm'],
                 'partofspeech': 'S',
                 'root': 'm<aa_<ilm'}],
   'text': 'maailm,'},
  {'analysis': [{'clitic': '',
                 'ending': '0',
                 'form': 'pl n',
                 'lemma': 'mis',
                 'lemma_tokens': ['mis'],
                 'partofspeech': 'P',
                 'root': 'mis'},
                {'clitic': '',
                 'ending': '0',
                 'form': 'sg n',
                 'lemma': 'mis',
                 'lemma_tokens': ['mis'],
                 'partofspeech': 'P',
                 'root': 'mis'}],
   'text': 'mis'},
  {'analysis': [{'clitic': '',
                 'ending': '0',
                 'form': '',
                 'lemma': 'teoksil',
                 'lemma_tokens': ['teoksil'],
                 'partofspeech': 'D',
                 'root': 't<eoksil'}],
   'text': 'teoksil?'}],
 [{'analysis': [{'clitic': '',
                 'ending': '0',
                 'form': '',
                 'lemma': 'täna',
                 'lemma_tokens': ['täna'],
                 'partofspeech': 'D',
                 'root': 'täna'},
                {'clitic': '',
                 'ending': '0',
                 'form': 'o',
                 'lemma': 'täna',
                 'lemma_tokens': ['täna'],
                 'partofspeech': 'V',
                 'root': 'täna'}],
   'text': 'Täna'},
  {'analysis': [{'clitic': '',
                 'ending': 'b',
                 'form': 'b',
                 'lemma': 'tule',
                 'lemma_tokens': ['tule'],
                 'partofspeech': 'V',
                 'root': 'tule'}],
   'text': 'tuleb'},
  {'analysis': [{'clitic': '',
                 'ending': '0',
                 'form': 'sg n',
                 'lemma': 'imeilus',
                 'lemma_tokens': ['ime', 'ilus'],
                 'partofspeech': 'A',
                 'root': 'ime_ilus'}],
   'text': 'imeilus'},
  {'analysis': [{'clitic': '',
                 'ending': '0',
                 'form': 'sg n',
                 'lemma': 'päev',
                 'lemma_tokens': ['päev'],
                 'partofspeech': 'S',
                 'root': 'p<äev'}],
   'text': 'päev!'}]]
```

