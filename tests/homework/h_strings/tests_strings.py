import unittest

from src.homework.h_strings.strings import get_hamming_distance, get_dna_compliment

class Test_Config(unittest.TestCase):

    def test_hamming_distance (self):
        self.assertEqual(get_hamming_distance('GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT'), 7)

    def test_compliment(self):
        self.assertEqual(get_dna_compliment('AAAACCCGGT'), 'ACCGGGTTTT')