PyVabamorf
==========

PyVabamorf is a Python interface for the Vabamorf Estonian lemmatizer and morphological analyzer/synthesizer.
Vabamorf is a open source morphological analyzer by Filosoft, which can be obtained from here: https://github.com/Filosoft/vabamorf .

# Analysis example

PyVabamorf takes the input string or a list of words and returns a list of dictionaries of possible analysis.

```
>>> from pyvabamorf import analyze
>>> from pprint import pprint
>>> pprint(analyze('Tüünete öötööde allmaaraudteejaam'))
[{'analysis': [{'clitic': '',
                'ending': 'te',
                'form': 'pl g',
                'lemma': 'tüüne',
                'partofspeech': 'A',
                'root': 't<üüne',
                'root_tokens': ['tüüne']}],
  'text': 'Tüünete'},
 {'analysis': [{'clitic': '',
                'ending': 'de',
                'form': 'pl g',
                'lemma': 'öötöö',
                'partofspeech': 'S',
                'root': '<öö_t<öö',
                'root_tokens': ['öö', 'töö']}],
  'text': 'öötööde'},
 {'analysis': [{'clitic': '',
                'ending': '0',
                'form': 'sg n',
                'lemma': 'allmaaraudteejaam',
                'partofspeech': 'S',
                'root': '<all_m<aa_r<aud_t<ee_j<aam',
                'root_tokens': ['all', 'maa', 'raud', 'tee', 'jaam']}],
  'text': 'allmaaraudteejaam'}]
```

Note that the underlying `vabamorf` library does not yet include disambiguation, so all possible analysis will be returned.

The synopsis for the ```analyze``` function is following:
```
def analyze(words, **kwargs):
    '''Perform morphological analysis on input.
    
    Parameters
    ----------
    words: list of str or str
        Either a list of pretokenized words or a string. In case of a string, it will be splitted using
        default behaviour of string.split() function.
    
    Keyword parameters
    ------------------
    guess: boolean
        If True, then use guessing, when analyzing unknown words (default: True)
    phonetic: boolean
        If True, add phonetic information to the root forms (default: True).
    compound: boolean
        if True, add compound word markers to root forms (default: True)

    Returns
    -------
    list of (list of dict)
        List of analysis for each word in input. One word usually contains more than one analysis as the
        analyser does not perform disambiguation.
```

# Synthesizer example

PyVabamorf is also capable of synthesizing words, given their lemma with POS tag and form.

```
>>> from pyvabamorf import synthesize
>>> synthesize('pood', form='pl p', partofspeech='S', phonetic=False)
['poode', 'poodisid']
>>> synthesize('palk', form='sg kom', phonetic=False)
['palgaga', 'palgiga']
>>> 
```

Some of the parameters are optional, so PyVabamorf synthesizes all possible variants it can.
The synopsis of ```synthesize``` function is following:

```
def synthesize(lemma, **kwargs):
    '''Given lemma, pos tag and a form, synthesize the word.

    Parameters
    ----------
    lemma: str
        The lemma of the word to be synthesized.
        
    Keyword parameters
    ------------------
    partofspeech: str
        The POS tag of the word to be synthesized.
    form: str
        The form of the word to be synthesized.
    hint: str
        The hint used by vabamorf to synthesize the word.
    guess: bool
        If True, use guessing for unknown words (default: True)
    phonetic: bool
        If True, add phonetic markers to synthesized words (default: True).
        
    Returns
    -------
    list of str
        The list of synthesized words.
    '''
```

# Installation

## Windows

Windows users can download pre-built binaries for latest `pyvabamorf` release:

### 32-bit

* https://github.com/tpetmanson/pyvabamorf/blob/master/dist/pyvabamorf-1.5.win32-py2.7.msi
* https://github.com/tpetmanson/pyvabamorf/blob/master/dist/pyvabamorf-1.5.win32-py3.4.msi

### 64-bit

* https://github.com/tpetmanson/pyvabamorf/blob/master/dist/pyvabamorf-1.5.win-amd64-py2.7.msi
* https://github.com/tpetmanson/pyvabamorf/blob/master/dist/pyvabamorf-1.5.win-amd64-py3.4.msi

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
$ python -m unittest discover pyvabamorf.tests
....................................
----------------------------------------------------------------------
Ran 36 tests in 0.446s

OK
```

# License

Pyvabamorf is licensed under LGPL. See LICENSE for details.
Copyright (c) by Filosoft OÜ and University of Tartu.
