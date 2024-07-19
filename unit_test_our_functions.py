import unittest
from our_functions import is_valid_date, is_valid_username

class TestOurFunctions(unittest.TestCase):
    def test_is_valid_date(self):
        # Valid dates
        self.assertTrue(is_valid_date("2023-07-16"))
        self.assertTrue(is_valid_date("2000-02-29"))  # Leap year
        self.assertTrue(is_valid_date("1900-02-28"))  # Non-leap year
        
        # Invalid dates
        self.assertFalse(is_valid_date(""))  # Empty string
        self.assertFalse(is_valid_date("2023-7-16"))  # Incorrect format
        self.assertFalse(is_valid_date("2023-13-01"))  # Invalid month
        self.assertFalse(is_valid_date("2023-12-32"))  # Invalid day
        self.assertFalse(is_valid_date("2023-02-29"))  # Non-leap year
        self.assertFalse(is_valid_date("abcd-ef-gh"))  # Non-numeric
        self.assertFalse(is_valid_date("2023-07-00"))  # Invalid day (zero)
        self.assertFalse(is_valid_date("2023-00-16"))  # Invalid month (zero)
        self.assertFalse(is_valid_date("0000-07-16"))  # Invalid year (below 1000)
        self.assertFalse(is_valid_date("10000-07-16"))  # Invalid year (above 9999)
        
    def test_is_valid_username(self):
        # Valid usernames
        self.assertTrue(is_valid_username("valid.username", 5))
        self.assertTrue(is_valid_username("valid_username", 5))
        self.assertTrue(is_valid_username("valid123", 5))
        self.assertTrue(is_valid_username("valid.username_123", 5))
        
        # Invalid usernames
        with self.assertRaises(TypeError):
            is_valid_username(12345, 5)
        with self.assertRaises(ValueError):
            is_valid_username("valid", 0)
        self.assertFalse(is_valid_username("short", 10))  # Too short
        self.assertFalse(is_valid_username("invalid username", 5))  # Spaces not allowed
        self.assertFalse(is_valid_username("invalid-username", 5))  # Hyphen not allowed
        self.assertFalse(is_valid_username("123username", 5))  # Starts with a number

if __name__ == "__main__":
    unittest.main()
