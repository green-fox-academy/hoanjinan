from zilan_work import Apple, Sum, Anagram, CountLetters, Fibonacci
import unittest

class TestingPerson(unittest.TestCase):
    def setUp(self):
        self.apple = Apple()
        self.sum = Sum(num_list = [1, 2, 3])
        self.anagram = Anagram()
        self.count_letters = CountLetters()
        self.fibonacci = Fibonacci()

    def test_apple(self):
        self.assertEqual(self.apple.get_apple("apple"), "apple")
    
    def test_sum(self):
        self.assertEqual(self.sum.total(), 6)

    def test_anagram(self):
        self.assertEqual(self.anagram.check_anagram("Hello", "World"), False)
        self.assertEqual(self.anagram.check_anagram("Hello", "Helol"), True)

    def test_count_letters(self):
        test_letter = "Hello"
        test_dictionary = {"H": 1, "e": 1, "l":2, "o":1}
        self.assertEqual(self.count_letters.count(test_letter), test_dictionary)

    def test_fibonacci(self):
        num_index = [1, 2, 5]
        range_index = [5, 7, 10]
        expected_result = [5, 26, 275]
        for i in range(len(num_index)):
            self.assertEqual(self.fibonacci.fibonacci_calculator(num_index[i], range_index[i]), expected_result[i])


    def tearDown(self):
        print("It runs after each test.")

if __name__ == "__main__":
    unittest.main()