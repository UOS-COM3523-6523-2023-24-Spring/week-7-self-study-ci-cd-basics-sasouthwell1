import unittest
from main import simple_count, complex_function
import random

class MyTestCase(unittest.TestCase):
    def test_simple_function1(self):
        self.assertEqual(0, simple_count(''))

    def test_simple_function2(self):
        self.assertEqual(5, simple_count('hello'))

    def test_complex_function(self):
        # Even though the behaviour is non deterministic, this random behaviour is seed dependent
        # Meaning that if we find the correct seed value, we can test the function and its behaviour
        random.seed(1514)
        self.assertEqual('behaviour 1', complex_function())
