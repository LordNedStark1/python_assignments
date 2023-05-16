from unittest import TestCase
from alx_learning import return_a_sum
from alx_learning import display

class Test(TestCase):
    def test_sum(self):
        list =[1,2,3,4,5]
        self.assertEqual(15, return_a_sum.sum_list(list))

    def test_display(self):
        new_list = [['O','X','O'],['X','O','O'],['X','O','X']]
        result = [[0,1,0],[1,0,0],[1,0,1]]
        self.assertEqual(result, display.display(new_list))
