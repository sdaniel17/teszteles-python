import unittest

def paros_szamok_ossz(x,y):
    osszeg = 0
    for i in range(x,y+1):
        if i%2 == 0:
            osszeg += i

    return osszeg

class TestParos(unittest.TestCase):
    def test_42_100(self):
        self.assertEqual(paros_szamok_ossz(42,100), 2130)

    def test_0_0(self):
        self.assertEqual(paros_szamok_ossz(0,0), 0)

    def test_2_10(self):
        self.assertEqual(paros_szamok_ossz(2,10), 30)

    def test_1_10(self):
        self.assertEqual(paros_szamok_ossz(1,10),30)

unittest.main()