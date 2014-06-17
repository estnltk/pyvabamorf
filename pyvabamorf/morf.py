# -*- coding: utf-8 -*-
import pyvabamorf.vabamorf as vm
import os
import six

PACKAGE_PATH = os.path.dirname(__file__)
DICT_PATH = os.path.join(PACKAGE_PATH, 'dct')

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

def wordtokens(word):
    '''Function that takes the root form of the word and parses it into tokens.
       For example '<all_m<aa_r<aud_t<ee_j<aosk<ond' would be parsed as ['all', 'maa', 'raud', 'tee', 'jaos', 'kond']
       '''
    if word == '<' or word == '_': # special case
        return word
    return word.replace('<', '').split('_')
    

class PyVabamorf(object):
    '''Class for performing main tasks of morphological analysis.'''

    def __init__(self, lexPath=DICT_PATH):
        self._analyzer = vm.Analyzer(lexPath)

    def _convert_sentence(self, sentence):
        '''This method converts the list of strings to appropriate encoding/type, depending
           on Python version.'''
        return [convert(word) for word in sentence]

    def _an_to_dict(self, an):
        '''Convert an analysis to dictionary.'''
        root = deconvert(an.root)
        ending = deconvert(an.ending)
        clitic = deconvert(an.clitic)
        pos = deconvert(an.partofspeech)
        form = deconvert(an.form)
        toks = wordtokens(root)
        lemma = u''.join(toks)
        return {'root': root,
               'ending': ending,
               'clitic': clitic,
               'partofspeech': pos,
               'form': form,
               'lemma': lemma,
               'lemma_tokens': toks}

    def analyze(self, sentence):
        '''Given an list of words, perform lemmatizartion and morphological analysis.
        
        Returns a list of dictionaries woth morphological analysis.
        
        Example:
        
        >>> from pyvabamorf import PyVabamorf
        >>> from pprint import pprint

        >>> m = PyVabamorf()
        >>> pprint(m.analyze('Tüüne öötöömiljöö allmaaraudteejaamas!'.split()))
        
        Output:
        
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
        '''


        sentence = self._convert_sentence(sentence)
        morfresult = self._analyzer.analyze(vm.StringVector(sentence))
        result = []
        for word, analysis in morfresult:
            analysis = [self._an_to_dict(an) for an in analysis]
            result.append({'text': deconvert(word),
                           'analysis': analysis})
        return result
    