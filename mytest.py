import unittest

from mycode import *


class Myfirsttest(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello_world(), 'hello world!')

    def test_custom_num_list(self):
        self.assertEqual(len(creat_num_list(10)),10)

        def test_custom_func_x(self):
            self.assertEqual(custom_func_x(3,2,3),54)