# -*- coding: utf-8 -*-
'''
Morphoanalysis functionality of pyvabamorf package.

Attributes
----------

PACKAGE_PATH: str
    The path where the pyvabamorf package is located.
DICT_PATH: str
    The path of the default vabamorf dictionary embedded with pyvabamorf.
phonetic_markers: str
    List of characters that make up phonetic markup.
compound_markers: str
    List of characters that make up compound markup.
markers: str
    List of characters of both phonetic and compound markup.
phonetic_regex: regex
    Regular expression matching any phonetic marker.
compound_regex: regex
    Regular expression matching any compound marker.
'''
from __future__ import unicode_literals, print_function

import pyvabamorf.vabamorf as vm
import os
import six
import re
import warnings

# path listings
PACKAGE_PATH = os.path.dirname(__file__)
DICT_PATH = os.path.join(PACKAGE_PATH, 'dct')

# various markers in 
phonetic_markers = '~?]<'
compound_markers = '_+=-'
markers = phonetic_markers + compound_markers
phonetic_regex = re.compile('|'.join([re.escape(c) for c in phonetic_markers]), flags=re.M)
compound_regex = re.compile('|'.join([re.escape(c) for c in compound_markers]), flags=re.M)


def convert(word):
    '''This method converts given `word` to appropriate encoding and type to be given to
       SWIG wrapper.'''
    if six.PY2:
        if isinstance(word, unicode):
            return word.encode('utf-8')
        else:
            return word.decode('utf-8').encode('utf-8') # make sure it is real utf8, otherwise complain
    else: # ==> Py3
        if isinstance(word, bytes):
            return word.decode('utf-8') # bytes must be in utf8
        return word

def deconvert(word):
    '''This method converts back the output from wrapper.
       Result should be `unicode` for Python2 and `str` for Python3'''
    if six.PY2:
        return word.decode('utf-8')
    else:
        return word

def trim_phonetics(root):
    '''Function that trims phonetic markup from the root.
    
    Parameters
    ----------
    root: str
        The string to remove the phonetic markup.
        
    Returns
    -------
    str
        The string with phonetic markup removed.
    '''
    global phonetic_markers
    global phonetic_regex
    if root in phonetic_markers:
        return root
    else:
        return phonetic_regex.sub('', root)

def tokenize(root):
    '''Function that takes the root form of the word and parses it into tokens.
    For example '<all_m<aa_r<aud_t<ee_j<aosk<ond' would be parsed as ['all', 'maa', 'raud', 'tee', 'jaos', 'kond']
    
    Parameters
    ----------
    root: str
        The root form of a word.

    Returns
    -------
    list of str
        List of root tokens
    '''
    global compound_markers
    global compound_regex
    if root in markers: # special case
        return [root]
    return [tok for tok in compound_regex.split(root) if len(tok) > 0]

def analysis_as_dict(an, trim_phonetic=True, trim_compound=True):
    '''Convert an analysis instance to a dictionary.
    Also adds "ma" ending to verbs.
    
    Parameters
    ----------
    an: vabamorf.WordAnalysis
        Analysis result as returned by vabamorf library.
    trim_phonetic: boolean
        If True, then removes phonetic annotations from root form. (default: True)
    trim_compound: boolean
        If True, then removes compund word annotations from root form. (default: True)
    
    Returns
    -------
    dict
        Morfoanalysis results.
    '''
    root = deconvert(an.root)
    
    # extract tokens and construct lemma
    toks = tokenize(trim_phonetics(root))
    lemma = ''.join(toks)
    if an.partofspeech == 'V':
        lemma += 'ma'
        
    # modify root form according to arguments
    if trim_phonetic:
        root = trim_phonetics(root)
    if trim_compound:
        root = ''.join(tokenize(root))
    
    return {'root': root,
            'root_tokens': toks,
            'ending': deconvert(an.ending),
            'clitic': deconvert(an.clitic),
            'partofspeech': deconvert(an.partofspeech),
            'form': deconvert(an.form),
            'lemma': lemma}

def get_args(**kwargs):
    '''Parse arguments from keyword parameters.
    
    Raises
    ------
    Exception
        In case an illegal argument is passed.
    
    Returns
    -------
    (boolean, boolean, boolean)
        Use heuristics, clean phonetics, clean compound.
    '''
    use_heuristics = True
    trim_phonetic = True
    trim_compound = True
    for key, value in kwargs.items():
        if key == 'use_heuristics':
            use_heuristics = bool(value)
        elif key == 'trim_phonetic':
            trim_phonetic = bool(value)
        elif key == 'trim_compound':
            trim_compound = bool(value)
        else:
            raise Exception('Unkown argument: {0}'.format(key))
    return (use_heuristics, trim_phonetic, trim_compound)
            
                
class PyVabamorf(object):
    '''Class for performing main tasks of morphological analysis.'''

    def __init__(self, lexPath=DICT_PATH):
        self._analyzer = vm.Analyzer(convert(lexPath))

    def analyze(self, words, **kwargs):
        '''Perform morphological analysis on input.
        
        Parameters
        ----------
        words: list of str or str
            Either a list of pretokenized words or a string. In case of a string, it will be splitted using
            default behaviour of string.split() function.
        
        Keyword parameters
        ------------------
        use_heuristics: boolean
            If True, then use heuristics, when analyzing unknown words (default: True)
        trim_phonetic: boolean
            If True, then removes phonetic annotations from root form. (default: True)
        trim_compound: boolean
            If True, then removes compund word annotations from root form. (default: True)

        Returns
        -------
        list of (list of dict)
            List of analysis for each word in input. One word usually contains more than one analysis as the
            analyser does not perform disambiguation.
        '''
        use_heuristics, trim_phonetic, trim_compound = get_args(**kwargs)
        
        # if input is a string, then tokenize it with whitespace
        if isinstance(words, six.string_types):
            words = words.split()
        
        # convert words to native string
        words = [convert(w) for w in words]
        
        # perform morphological analysis
        morfresult = self._analyzer.analyze(vm.StringVector(words), use_heuristics)
        result = []
        for word, analysis in morfresult:
            analysis = [analysis_as_dict(an, trim_phonetic, trim_compound) for an in analysis]
            result.append({'text': deconvert(word),
                           'analysis': analysis})
        return result
    
def analyze(words, **kwargs):
    '''Perform morphological analysis on input.
    
    Parameters
    ----------
    words: list of str or str
        Either a list of pretokenized words or a string. In case of a string, it will be splitted using
        default behaviour of string.split() function.
    
    Keyword parameters
    ------------------
    use_heuristics: boolean
        If True, then use heuristics, when analyzing unknown words (default: True)
    trim_phonetic: boolean
        If True, then removes phonetic annotations from root form. (default: True)
    trim_compound: boolean
        If True, then removes compund word annotations from root form. (default: True)

    Returns
    -------
    list of (list of dict)
        List of analysis for each word in input. One word usually contains more than one analysis as the
        analyser does not perform disambiguation.
    '''
    if not hasattr(analyze, 'pid') or analyze.pid != os.getpid():
        analyze.pid = os.getpid()
        analyze.morf = PyVabamorf()
        
    return analyze.morf.analyze(words, **kwargs)

