# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
from pyvabamorf import analyze
from pyvabamorf.morf import tokenize, analysis_as_dict, convert, deconvert
from pyvabamorf.vabamorf import Analysis
from pprint import pprint

class Tokenizetest(unittest.TestCase):
    '''Testcase for removal of wierd helper characters in vabamorf output.'''

    def test_intsident(self):
        tokens = tokenize('?intsiden]t')
        self.assertListEqual(tokens, ['intsident'])

    def test_edastatud(self):
        tokens = tokenize('edasta=tud')
        self.assertListEqual(tokens, ['edastatud'])

    def test_withall(self):
        tokens = tokenize('all_+maa_raud]_tee_jaam?')
        self.assertListEqual(tokens, ['all', 'maa', 'raud', 'tee', 'jaam'])
        
    def test_underscore(self):
        tokens = tokenize('_')
        self.assertListEqual(tokens, ['_'])
        
    def test_plus(self):
        tokens = tokenize('+')
        self.assertListEqual(tokens, ['+'])
        
    def test_equalmark(self):
        tokens = tokenize('=')
        self.assertListEqual(tokens, ['='])
    
    def test_ltmark(self):
        tokens = tokenize('<')
        self.assertListEqual(tokens, ['<'])
   
    def test_bracketclose(self):
        tokens = tokenize(']')
        self.assertListEqual(tokens, [']'])


class AnalysisAsDictTest(unittest.TestCase):
    
    def test_verb_nocleanroot(self):
        self.assertDictEqual(analysis_as_dict(self.verb(), False), self.verb_nocleanroot())
    
    def test_verb_cleanroot(self):
        self.assertDictEqual(analysis_as_dict(self.verb(), True), self.verb_cleanroot())
    
    def test_substantive_nocleanroot(self):
        self.assertDictEqual(analysis_as_dict(self.substantive(), False), self.substantive_nocleanroot())
    
    def test_substantive_cleanroot(self):
        self.assertDictEqual(analysis_as_dict(self.substantive(), True), self.substantive_cleanroot())
    
    def verb(self):
        return Analysis(convert('l<aul'),
                        convert('b'),
                        convert(''),
                        convert('V'),
                        convert('b'))
    
    def substantive(self):
        return Analysis(convert('lennuki_k<an]dja'),
                        convert('ile'),
                        convert(''),
                        convert('S'),
                        convert('pl all'))

    def verb_nocleanroot(self):
        return {'clitic': '',
                'ending': 'b',
                'form': 'b',
                'lemma': 'laulma',
                'partofspeech': 'V',
                'root_tokens': ['laul'],
                'root': 'l<aul'}
    
    def verb_cleanroot(self):
        return {'clitic': '',
                'ending': 'b',
                'form': 'b',
                'lemma': 'laulma',
                'partofspeech': 'V',
                'root_tokens': ['laul'],
                'root': 'laul'}

    def substantive_nocleanroot(self):
        return {'clitic': '',
                'ending': 'ile',
                'form': 'pl all',
                'lemma': 'lennukikandja',
                'partofspeech': 'S',
                'root_tokens': ['lennuki', 'kandja'],
                'root': 'lennuki_k<an]dja'}

    def substantive_cleanroot(self):
        return {'clitic': '',
                'ending': 'ile',
                'form': 'pl all',
                'lemma': 'lennukikandja',
                'partofspeech': 'S',
                'root_tokens': ['lennuki', 'kandja'],
                'root': 'lennukikandja'}

                
class TextIsSameAsListTest(unittest.TestCase):
    
    def test_text_is_same_no_heuristics_noclean_root(self):
        self.run_test(False, False)
        
    def test_text_is_same_heuristics_noclean_tooy(self):
        self.run_test(True, False)

    def test_text_is_same_no_heuristics_clean_root(self):
        self.run_test(False, True)
        
    def test_text_is_same_heuristics_clean_tooy(self):
        self.run_test(True, True)
    
    def run_test(self, use_heuristics, clean_root):
        text_output = analyze(self.text(),
                                use_heuristics=use_heuristics,
                                clean_root=clean_root)
        list_output = analyze(self.text().split(),
                                use_heuristics=use_heuristics,
                                clean_root=clean_root)
        self.assertListEqual(text_output, list_output)
    
    def text(self):
        # http://luuletused.ee/1005/elu/hetke-volu
        return '''Ma tahaks suudelda päikesekiiri 
                vat nii ihalevad mu huuled päikese suule.. 
                Ma tahaks tantsida kesksuvises vihmas 
                vat nii tunglevad minu tunded südames suures 

                Keegi kord ütles, et ära karda 
                armastus saab aja jooksul ainult kasvada 
                Võta kõik vastu, mis sulle pakutakse, 
                sest see, mis sulle antakse 
                on sinu jaoks loodud'''


                
if __name__ == '__main__':
    unittest.main()
