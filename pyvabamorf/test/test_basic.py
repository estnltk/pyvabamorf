# -*- coding: utf-8 -*-
import unittest
from pyvabamorf import analyze_sentence
from pyvabamorf.morf import wordtokens

class TestBasic(unittest.TestCase):
    
    def test_analyze_sentence(self):
        res = analyze_sentence(self.analyze_input())
        self.assertListEqual(res, self.analyze_result())
    
    def test_nonunicode_analuze_fails(self):
        self.assertRaises(Exception, analyze_sentence, (self.invalid_analyze_input()))

    def test_empty_input_yields_empty_output(self):
        self.assertEqual(len(analyze_sentence([])), 0)
    
    def analyze_input(self):
        return u'Tüüne öötöömiljöö allmaaraudteejaamas!'.split()
    
    def invalid_analyze_input(self):
        return u'Tüüne öötöömiljöö allmaaraudteejaamas!'.encode('latin-1').split()
    
    def analyze_result(self):
        return [{'analysis': [{'clitic': u'',
                        'ending': u'0',
                        'form': u'sg g',
                        'lemma': u'tüün',
                        'lemma_tokens': [u'tüün'],
                        'partofspeech': u'A',
                        'root': u't<üün'},
                    {'clitic': u'',
                        'ending': u'0',
                        'form': u'sg g',
                        'lemma': u'tüüne',
                        'lemma_tokens': [u'tüüne'],
                        'partofspeech': u'A',
                        'root': u't<üüne'},
                    {'clitic': u'',
                        'ending': u'0',
                        'form': u'sg n',
                        'lemma': u'tüüne',
                        'lemma_tokens': [u'tüüne'],
                        'partofspeech': u'A',
                        'root': u't<üüne'}],
        'text': u'Tüüne'},
        {'analysis': [{'clitic': u'',
                        'ending': u'0',
                        'form': u'sg g',
                        'lemma': u'öötöömiljöö',
                        'lemma_tokens': [u'öö', u'töö', u'miljöö'],
                        'partofspeech': u'S',
                        'root': u'<öö_t<öö_milj<öö'},
                    {'clitic': u'',
                        'ending': u'0',
                        'form': u'sg n',
                        'lemma': u'öötöömiljöö',
                        'lemma_tokens': [u'öö', u'töö', u'miljöö'],
                        'partofspeech': u'S',
                        'root': u'<öö_t<öö_milj<öö'}],
        'text': u'öötöömiljöö'},
        {'analysis': [{'clitic': u'',
                        'ending': u's',
                        'form': u'sg in',
                        'lemma': u'allmaaraudteejaam',
                        'lemma_tokens': [u'all', u'maa', u'raud', u'tee', u'jaam'],
                        'partofspeech': u'S',
                        'root': u'<all_m<aa_r<aud_t<ee_j<aam'}],
        'text': u'allmaaraudteejaamas!'}]


class TestWordTokens(unittest.TestCase):
    '''Testcase for removal of wierd helper characters in vabamorf output.'''

    def test_intsident(self):
        tokens = wordtokens(u'?intsiden]t')
        self.assertListEqual(tokens, [u'intsident'])

    def test_edastatud(self):
        tokens = wordtokens(u'edasta=tud')
        self.assertListEqual(tokens, [u'edastatud'])

    def test_withall(self):
        tokens = wordtokens(u'all_+maa_raud]_tee_jaam?')
        self.assertListEqual(tokens, [u'all', u'maa', u'raud', u'tee', u'jaam'])
        
    def test_underscore(self):
        tokens = wordtokens(u'_')
        self.assertListEqual(tokens, [u'_'])
        
    def test_plus(self):
        tokens = wordtokens(u'+')
        self.assertListEqual(tokens, [u'+'])
        
    def test_equalmark(self):
        tokens = wordtokens(u'=')
        self.assertListEqual(tokens, [u'='])
    
    def test_ltmark(self):
        tokens = wordtokens(u'<')
        self.assertListEqual(tokens, [u'<'])
   
    def test_bracketclose(self):
        tokens = wordtokens(u']')
        self.assertListEqual(tokens, [u']'])

