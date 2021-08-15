import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """Tests for name_function.py"""

    def test_first_name_and_last_name (self):
        """Does the function work"""
        formatted_name = get_formatted_name("ali", "mushtaq")
        self.assertEqual(formatted_name, 'Ali Mushtaq')

unittest.main()