import unittest
from main import NumberList

class TestNumberList(unittest.TestCase):

    def test_iteration(self):
        numbers = NumberList([1, 2, 3, 4, 5])
        iterator = iter(numbers)

        self.assertEqual(next(iterator), 1)
        self.assertEqual(next(iterator), 2)
        self.assertEqual(next(iterator), 3)
        self.assertEqual(next(iterator), 4)
        self.assertEqual(next(iterator), 5)
        self.assertEqual(next(iterator), "Error: last iterator already been.")

if __name__ == '__main__':
    unittest.main()