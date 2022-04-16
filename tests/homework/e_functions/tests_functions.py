import unittest

from src.homework.e_functions.value_return import get_hour
from src.homework.e_functions.value_return import get_minutes
from src.homework.e_functions.value_return import get_seconds
from src.homework.e_functions.value_return import time_from_utc

class Test_Config(unittest.TestCase):

    def test_hour(self):
        self.assertEqual(get_hour(4200), 1)
    
    def test_minutes(self):
        self.assertEqual(get_minutes(7400), 3)
    
    def test_seconds(self):
        self.assertEqual(get_seconds(3650), 50)

    def test_utc_time(self):
        self.assertEqual(time_from_utc(20, -5), 15)