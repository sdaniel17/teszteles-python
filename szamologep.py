import unittest

def szamologep(elso_szam:float, masodik_szam:float, muvelet:str):
    if muvelet == "+":
        return(elso_szam+masodik_szam)
    elif muvelet == "-":
        return(elso_szam-masodik_szam)
    elif muvelet == "*":
        return(round(elso_szam*masodik_szam, 2))
    elif muvelet == "/":
        if masodik_szam == 0:
            return "Ejnye, nullaval nem osztunk!"
        else:
            return(round(elso_szam/masodik_szam, 2))
    else:
        return("Hibas muveleti jel!")

class TestSzamologep(unittest.TestCase):

    def test_3oszt0(self):
        self.assertEqual(szamologep(3,0,"/"), "Ejnye, nullaval nem osztunk!")
    def test_3plus3(self):
        self.assertEqual(szamologep(3,3,"_"), "Hibas muveleti jel!")
    def test_3szor3(self):
        self.assertGreater(szamologep(3,3,"*"), 8)
    def test_3bol3(self):
        self.assertLess(szamologep(3,3,"-"), 3)
    def test_3plusz3(self):
        self.assertGreater(szamologep(3,3,"+"), 2)
    def test_3oszt3(self):
        self.assertLess(szamologep(3,3,"/"), 9)
    def test_3minuszminusz3(self):
        self.assertGreater(szamologep(3,-3,"-"),1)
    def test_3szorminusz3(self):
        self.assertLess(szamologep(3,-3,"*"), 0)
    def test_3osztminusz3(self):
        self.assertLess(szamologep(3,-3,"/"),0)
    def test_minusz3szorminusz3(self):
        self.assertGreater(szamologep(-3,-3,"*"),0)
    def test_minusz3oszt3(self):
        self.assertLess(szamologep(-3,3,"/"),0)
unittest.main()