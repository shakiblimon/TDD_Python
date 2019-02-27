import unittest

from mycode import *


class Myfirsttest(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello_world(), 'hello world!')

#   test custome number list
    def test_custom_num_list(self):
        self.assertEqual(len(creat_num_list(10)), 10)

#   test cusrome function x
    def test_custom_func_x(self):
        self.assertEqual(custom_func_x(3, 2, 3), 54)


#    test custome non linear number list
    def test_custom_non_lin_num_list(self):
        self.assertEqual(custom_non_lin_num_list(5,2,3)[2],16)
        self.assertEqual(custom_non_lin_num_list(5,2,3)[4],48)