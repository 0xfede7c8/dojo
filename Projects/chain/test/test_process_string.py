import unittest

from ..process_string import validate_string


class MyTestCase(unittest.TestCase):
    def test_upper(self):
        self.assertRaises(Exception, validate_string, 'Hello')

    def test_empty(self):
        self.assertRaises(Exception, validate_string, '')

    def test_length(self):
        self.assertRaises(Exception, validate_string, 'a' * 101)


if __name__ == '__main__':
    unittest.main()
