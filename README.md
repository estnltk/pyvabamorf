PyVabamorf
==========

PyVabamorf is a Python interface for the Vabamorf Estonian lemmatizer and morphological analyzer.
Vabamorf is a open source morphological analyzer by Filosoft, which can be obtained from here: https://github.com/Filosoft/vabamorf .

# Example

```
>>> from pyvabamorf import analyze
>>> from pprint import pprint
>>> pprint(analyze('Usjas kaslane jookseb maastikul'))
[{'analysis': [{'clitic': '',
                'ending': '0',
                'form': 'sg n',
                'lemma': 'usjas',
                'partofspeech': 'A',
                'root': 'usjas',
                'root_tokens': ['usjas']},
               {'clitic': '',
                'ending': 's',
                'form': 'sg in',
                'lemma': 'usjas',
                'partofspeech': 'A',
                'root': 'usjas',
                'root_tokens': ['usjas']}],
  'text': 'Usjas'},
 {'analysis': [{'clitic': '',
                'ending': '0',
                'form': 'sg n',
                'lemma': 'kaslane',
                'partofspeech': 'S',
                'root': 'kaslane',
                'root_tokens': ['kaslane']}],
  'text': 'kaslane'},
 {'analysis': [{'clitic': '',
                'ending': 'b',
                'form': 'b',
                'lemma': 'jooksma',
                'partofspeech': 'V',
                'root': 'jooks',
                'root_tokens': ['jooks']}],
  'text': 'jookseb'},
 {'analysis': [{'clitic': '',
                'ending': 'l',
                'form': 'sg ad',
                'lemma': 'maastik',
                'partofspeech': 'S',
                'root': 'maastik',
                'root_tokens': ['maastik']}],
  'text': 'maastikul'}]
```

The `analysis` function expects the input as a string or a list of strings. The following commands are equivalent:
```
analyze('Usjas kaslane jookseb maastikul')
analyze('Usjas kaslane jookseb maastikul'.split())
analyze(['Usjas', 'kaslane', 'jookseb', 'maastikul'])
```
In case of a string, `pyvabamorf` just uses default `split()` function to tokenize the text.

The output is a list, one per word, containing one or more dictionaries with different analysis. Note that the underlying `vabamorf` library does not yet include disambiguation, so all possible analysis will be returned.

## Heuristics

By default, `pyvabamorf` has enabled heuristics, which are used to analyze unknown words. Heuristics can be disabled by passing the `analyze` function the argument `use_heuristics=False`.

```
>>> pprint(analyze('seeontundmatuile'))
[{'analysis': [{'clitic': '',
                'ending': 'ile',
                'form': 'pl all',
                'lemma': 'seeontundmatu',
                'partofspeech': 'S',
                'root': 'seeontundmatu',
                'root_tokens': ['seeontundmatu']}],
  'text': 'seeontundmatuile'}]
>>> pprint(analyze('seeontundmatuile', use_heuristics=False))
[{'analysis': [], 'text': 'seeontundmatuile'}]
```

## Cleaned root forms

By default, `pyvabamorf` removes extra annotation from analyzed root forms. This can be disabled by using argument `clean_root=False`.

```
>>> pprint(analyze('allmaaraudteedele'))
[{'analysis': [{'clitic': '',
                'ending': 'dele',
                'form': 'pl all',
                'lemma': 'allmaaraudtee',
                'partofspeech': 'S',
                'root': 'allmaaraudtee',
                'root_tokens': ['all', 'maa', 'raud', 'tee']}],
  'text': 'allmaaraudteedele'}]
>>> pprint(analyze('allmaaraudteedele', clean_root=False))
[{'analysis': [{'clitic': '',
                'ending': 'dele',
                'form': 'pl all',
                'lemma': 'allmaaraudtee',
                'partofspeech': 'S',
                'root': '<all_m<aa_r<aud_t<ee',
                'root_tokens': ['all', 'maa', 'raud', 'tee']}],
  'text': 'allmaaraudteedele'}]
```

# Installation

## Windows

Windows users can download pre-built binaries for latest `pyvabamorf` release:

### 32-bit

* https://github.com/tpetmanson/pyvabamorf/blob/master/dist/pyvabamorf-1.4.win32-py2.7.msi
* https://github.com/tpetmanson/pyvabamorf/blob/master/dist/pyvabamorf-1.4.win32-py3.4.msi

### 64-bit

* https://github.com/tpetmanson/pyvabamorf/blob/master/dist/pyvabamorf-1.4.win-amd64-py2.7.msi
* https://github.com/tpetmanson/pyvabamorf/blob/master/dist/pyvabamorf-1.4.win-amd64-py3.4.msi

### Building from source.

To build the `pyvabamorf` module from source, we recommend using Visual Studio 2008 for Python2.7 and Visual Studio 2010 for Python3.4. Note that for 64-bit versions you need to have also 64-bit toolchains, which are not included in Express versions of the Visual Studio.

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

Then run the tests and see if they all pass (NB! Do not run them from same directory you have cloned the source distribution):
```
python -m unittest discover pyvabamorf.test

.................
----------------------------------------------------------------------
Ran 17 tests in 0.518s

OK
```

# License

Pyvabamorf is licensed under LGPL. See LICENSE for details.
Copyright (c) by Filosoft OÜ and University of Tartu.
