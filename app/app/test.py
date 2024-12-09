"""To test the code"""

from django.test import SimpleTestCase

from app import calc


class CalcTest(SimpleTestCase):
    """Test the calc module."""

    def test_add_number(self):
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        res = calc.subtract(5, 6)

        self.assertEqual(res, 1)
