import unittest

from src.helpers import get_distance


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(get_distance([10,80],[0,80]), 10.0)

if __name__ == '__main__':
    unittest.main()