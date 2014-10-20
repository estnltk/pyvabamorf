# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import pyvabamorf.vabamorf as vm
import os
import six
import re
import warnings

PACKAGE_PATH = os.path.dirname(__file__)
DICT_PATH = os.path.join(PACKAGE_PATH, 'dct')

markers = ['?', '<', '=', '+', ']', '_']
tokenize_regex = re.compile('[?<=+\]]')

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
    global markers
    global tokenize_regex
    if root in markers: # special case
        return [root]
    return tokenize_regex.sub('', root).split('_')

def analysis_as_dict(an, clean_root):
    '''Convert an analysis instance to a dictionary.
    Also adds "ma" ending to verbs.
    
    Parameters
    ----------
    an: vabamorf.WordAnalysis
        Analysis result as returned by vabamorf library.
    clean_root: boolean
        If True, then removes extra annotations from root form.
    
    Returns
    -------
    dict
        Morfoanalysis results.
    '''
    root = deconvert(an.root)
    toks = tokenize(root)
    lemma = ''.join(toks)
    if clean_root:
        root = lemma
    if an.partofspeech == 'V':
        lemma += 'ma'
    return {'root': root,
            'root_tokens': toks,
            'ending': deconvert(an.ending),
            'clitic': deconvert(an.clitic),
            'partofspeech': deconvert(an.partofspeech),
            'form': deconvert(an.form),
            'lemma': lemma}

def get_args(**kwargs):
    '''Check for illegal arguments.
    
    Returns
    -------
    (boolean, boolean)
        Settings respectively for use_heuristics and clean_root.
    '''
    use_heuristics = True
    clean_root     = True
    for key, value in kwargs.items():
        if key == 'use_heuristics':
            use_heuristics = bool(value)
        elif key == 'clean_root':
            clean_root = bool(value)
        else:
            raise Exception('Unkown argument: {0}'.format(key))
    return (use_heuristics, clean_root)
            
                
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
        clean_root: boolean
            If True, remove extra markers from root form (default: True)

        Returns
        -------
        list of (list of dict)
            List of analysis for each word in input. One word usually contains more than one analysis as the
            analyser does not perform disambiguation.
        '''
        use_heuristics, clean_root = get_args(**kwargs)
        
        # if input is a string, then tokenize it with whitespace
        if isinstance(words, six.string_types):
            words = words.split()
        
        # convert words to native string
        words = [convert(w) for w in words]
        
        # perform morphological analysis
        morfresult = self._analyzer.analyze(vm.StringVector(words), use_heuristics)
        result = []
        for word, analysis in morfresult:
            analysis = [analysis_as_dict(an, clean_root) for an in analysis]
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
    clean_root: boolean
        If True, remove extra markers from root form (default: True)

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

