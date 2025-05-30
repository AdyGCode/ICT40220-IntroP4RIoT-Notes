from unittest import TestCase

from calculations import Calculations


class TestCalculations(TestCase):

    def test_add_two_numbers(self):
        calculator = Calculations()
        self.assertEqual(3, calculator.add(1, 2))
        self.assertEqual(3, calculator.add(1, 2))
        self.assertEqual(0 + 4j, calculator.add(1, -1 + 4j))

    def test_value_error(self):
        calculator = Calculations()
        self.assertRaises(ValueError, calculator.add, 1, True)
        self.assertRaises(ValueError, calculator.add, True, True)
        self.assertRaises(ValueError, calculator.add, 0, "test")
