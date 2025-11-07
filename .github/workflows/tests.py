# .github/workflows/tests.py
import unittest

class My_Test(unittest.TestCase):
    def test_my_Test(self):
        print("hello World")
        print(" This is me pushing to see if it works")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
