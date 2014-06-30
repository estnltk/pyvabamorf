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

Alternatively, you can use _pip_ tool to download and install the library from Python Package Index (PyPI). You still need to install necessary dependencies to build the package.

```
sudo pip install pyvabamorf
```

Then run the tests and see if they all pass (NB! Don't run them from same directory you have cloned the source distribution):
```
python -m unittest discover pyvabamorf.test
```

PyVabamorf should work with both Python 2.x and Python 3.x versions, although we have tested it
currently only with Python 2.7 and Python 3.3.


## Binary packages

We plan to release precompiled and easily installable packages for both 32 and 64 bit versions of Linux and Windows.

# Usage examples

## Morphological analysis and lemmatization

Python3 code:
```python
from pyvabamorf import analyze_sentence
from pprint import pprint

pprint(analyze_sentence('Tüüne öötöömiljöö allmaaraudteejaamas!'.split()))
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

