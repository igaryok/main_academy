'''
tests for request_re.py
'''

import unittest

import requests_re


class Test(unittest.TestCase):

    def test_privat_api(self):
        check_list = requests_re.get_pb_rates()
        for each in check_list:
            self.assertTrue(each[0].isalpha())
            self.assertTrue(each[1].isalpha())
            self.assertTrue(each[2].replace(".", "").replace(",", "").isdigit())

    def test_cbr_api(self):
        check_list = requests_re.get_cbr_rates()
        for each in check_list:
            self.assertTrue(each[0].isalpha())
            self.assertTrue(each[1].isdigit())
            self.assertNotEqual(int(each[1]), 0)
            self.assertTrue(each[2].replace(".", "").replace(",", "").isdigit())


if __name__ == '__main__':
    unittest.main()
