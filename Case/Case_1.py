# -*- coding: utf-8 -*-
import unittest
from Bussinesslib.Doclever import Docleverlib

class DoTestCase(unittest.TestCase):
    def setUp(self):
        self.Doclever = Docleverlib()
        self.Doclever.run_driver()

    def test_login(self):
        self.Doclever.login()
        self.assertEqual(True,self.Doclever.is_element_present('id=tab-interface'))


    def tearDown(self):
        self.Doclever.close_driver()

if __name__ == "__main__":
    unittest.main()