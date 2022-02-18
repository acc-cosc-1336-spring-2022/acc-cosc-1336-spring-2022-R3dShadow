import unittest

from src.homework.c_decisions.decisions import get_options_ratio
from src.homework.c_decisions.decisions import get_faculty_rating

class Test_Config(unittest.TestCase):
    def test_get_options_ratio(self):
        self.assertEqual(0.25, 5 / 20)
        self.assertEqual(0.5, 10 / 20)
        if get_options_ratio == 0.25:
            return True
        if get_options_ratio == 0.5:
            return True

    def test_get_faculty_rating(self):
        if get_faculty_rating == 0.91:
            return 'Excellent'
        if get_faculty_rating ==0.85:
            return 'Very Good'
        if get_faculty_rating == 0.71:
            return 'Good'
        if get_faculty_rating == 0.66:
            return 'Unacceptable'
    