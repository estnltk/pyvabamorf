# -*- coding: utf-8 -*-
import unittest
from pyvabamorf import analyze_sentence


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

