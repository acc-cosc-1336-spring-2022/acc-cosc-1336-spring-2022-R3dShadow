#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())



#question d
import unittest

from src.question_a.question_a import get_person_category
from src.question_b.question_b import get_sum_of_events
from src.question_c.question_c import get_bonus_pay_amount
from src.question_d.question_d import get_assesment_value, get_tax_assessed

class Test_Config(unittest.TestCase):

    def test_age(self):
        self.assertEqual(get_person_category(125), 'Invalid number')

    def test_sum(self):
        self.assertEqual(get_sum_of_events(8), 20)
    
    def test_bonus(self):
        self.assertEqual(get_bonus_pay_amount(1500), 120)

    def test_value(self):
        self.assertEqual(get_assesment_value(10000), 6000)
    
    def test_tax(self):
        self.assertEqual(get_tax_assessed(10000), 72)

