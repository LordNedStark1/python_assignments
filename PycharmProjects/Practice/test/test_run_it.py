from unittest import TestCase
from alx_learning import run_it

class Test(TestCase):
    def test_method(self):
        numbers = [12, 3, 6, 20]
        result = [20, 6, 3, 12]

        self.assertListEqual(result, run_it.method(numbers))
