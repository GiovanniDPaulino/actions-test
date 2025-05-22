import unittest
from calculator import add

class TestCalculator(unittest.TestCase):

    def testAdd(self):

        #setup
        first = 2
        second = 3
        expected = 5

        #invoke
        actual = add(first, second)

        #analyze
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()