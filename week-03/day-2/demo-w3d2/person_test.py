from person import Person
import unittest

class TestingPerson(unittest.TestCase):
    def setUp(self):
        self.john = Person("John")
        self.jane = Person("Jane")

    def test_str_person(self):
        self.assertEqual(str(self.john), "I'm John and I'm hungry.")

    def test_eat(self):
        self.assertTrue(self.john.is_hungry())
        self.john.eat(8)
        self.assertFalse(self.john.is_hungry())

    def test_greet_person(self):
        self.assertEqual(self.john.greet(self.jane), "Hello, Jane!")

    def tearDown(self):
        print("It runs after each test.")

if __name__ == "__main__":
    unittest.main()