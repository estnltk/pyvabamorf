# -*- coding: utf-8 -*-
import unittest
from pyvabamorf import PyVabamorf

class TestBasic(unittest.TestCase):
    
    def setUp(self):
        self.morf = PyVabamorf()
    
    def test_analyze(self):
        self.morf.analyze(u'Tüüne öötöömiljoo allmaaraudteejaamas'.split())
    
    def test_nonunicode_analuze_fails(self):
        self.assertRaises(Exception, self.morf.analyze, (u'Tüüne öötöömiljoo allmaaraudteejaamas'.encode('latin-1').split()))
