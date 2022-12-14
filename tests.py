import unittest

from Calculator import Calculator


class testCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_sum(self):
        self.assertEqual(self.calculator.sum(4, 2), 6)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(10, 8), 2)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(7, 5), 35)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(10, 2), 5)


if __name__ == "__main__":
  unittest.main()


