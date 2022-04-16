import unittest

from src.homework.i_dictionaries_sets.dictionary import get_p_distance

class Test_Config(unittest.TestCase):

    def test_distance(self):
        self.assertEqual(get_p_distance('TTTCCATTTA', 'TTACCTATTA'), .3)