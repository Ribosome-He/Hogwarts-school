import unittest

def add(x,y):
    return x+y

class ACase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("classmethod")

    def test_case1(self):
        print("case1")
        self.assertEqual(add(9,1),10)

    def test_case2(self):
        print("case2")
        self.assertEqual(add(5,1),7)

    def tearDown(self):
        print("testDown")

    @classmethod
    def tearDownClass(cls):
        print("teardownclass")


if __name__ == '__main__':
    print("hhhh")
    unittest.main()