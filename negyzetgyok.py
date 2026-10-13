from math import sqrt
import unittest

def negyzetgyok(x):
    return sqrt(x)

class TestSqrt(unittest.TestCase):

    def test_1(self):
        self.assertEqual(negyzetgyok(4), 2)

    def test_2(self):
        self.assertEqual(negyzetgyok(25), 5)

unittest.main()