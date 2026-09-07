import unittest
from example import greet, add, multiply


class TestExample(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")
        self.assertEqual(greet("Bob"), "Hello, Bob!")

    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-1, 1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(4, 6), 24)
        self.assertEqual(multiply(-2, 3), -6)

if __name__ == "__main__":
    unittest.main()