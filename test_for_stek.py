import unittest
from parser_for_term import two_stek_parser

class TestStek(unittest.TestCase):
    def test_one(self):
        self.assertEqual(two_stek_parser("1+1"), 2.0)

    def test_two(self):
        self.assertEqual(two_stek_parser('(1+1)*2-3'), 1.0)

    def test_three(self):
        self.assertEqual(two_stek_parser('(1.+1))*2-3'), None)







