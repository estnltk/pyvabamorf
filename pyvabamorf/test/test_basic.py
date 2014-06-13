import unittest
from pyvabamorf import PyVabamorf

class TestBasic(unittest.TestCase):
    
    def setUp(self):
        morf = PyVabamorf()
    
    def test_analyze(self):
        morf.analyze(u'Ööd on siin pimedad'.split())
    
    def test_nonunicode_analuze_fails(self):
        self.assertRaises(AssertionError, morf.analyze, ('Ööd on siin pimedad'.split())

