# -*- coding: utf-8 -*-
import unittest
from pyvabamorf import analyze_sentence
from multiprocessing import Pool

class MultiProcessingAnalysisTest(unittest.TestCase):

    def test_ten_processes(self):
        pool = Pool(10)
        self.assertListEqual(pool.map(analyze_sentence, self.inputs()),
                             map(analyze_sentence, self.inputs()))
    
    def inputs(self):
        return [u'Selle testi eesmärk on katsetada, kas meil õnnestub vabamorfi teeki kasutada paralleelselt.'.split(),
                u'Esimese asjana jooksutame kogu sisendi läbi ühe lõime ning seejärel jooksutame seda Pythoni Pool klassi abil.'.split(),
                u'Viimane peaks tekitama mitu lõime ( sh. on oluline et vabamorfi initsialiseerimine toimiks).'.split(),
                u'Kuna vabamorf teisendab protsessi tasandil kõik sõned unikaalseteks identifikaatoriteks, tahame, et igal uuel protsessil oleks see unikaalne'.split(),
                u'Sellel eesmärgil jooksutame ka seda testi'.split()]*50

