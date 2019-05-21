from mymath import add
import unittest

class TestMyMathMethods(unittest.TestCase):
    def test_add_with_positive_integers(self):
        actual = add(2, 3)
        expected = 5
        self.assertEqual(actual, expected, "2 + 3 must be 5")
        self.assertEqual(add(5, 5), 10)

    def test_add_with_negative_floats(self):
        self.assertEqual(add(-2.5, -1.0), -3.5)

    def test_add_with_complex_numbers(self):
        self.assertEqual(add(0 + 0j, 1+0j), 1 + 0j)


if __name__ == "__main__":
    unittest.main()