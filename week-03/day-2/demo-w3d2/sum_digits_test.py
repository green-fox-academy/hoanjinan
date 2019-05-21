import unittest
from sum_digits import sumd

class TestingSumDigits(unittest.TestCase):
    def test_existance(self):
        sumd(1)

    def test_one(self):
        self.assertEqual(sumd(1), 1)

    def test_two(self):
        self.assertEqual(sumd(2), 2)

    def test_single_digits(self):
        for i in range(10):
            self.assertEqual(sumd(i), i)

if __name__ == "__main__":
    unittest.main()