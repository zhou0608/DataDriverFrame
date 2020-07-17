# -*- coding: utf-8 -*-
import unittest
from Bussinesslib.Doclever import Docleverlib

class DoTestCase(unittest.TestCase):
    def setUp(self):
        self.Doclever = Docleverlib()
        self.Doclever.run_driver()

    def test_1(self):
        self.Doclever.login('zhou952789','123456')
        self.assertTrue(self.Doclever.is_element_present('id=tab-interface'))

    def test_2(self):
        self.Doclever.login('zhou952789','12456')
        self.assertTrue(self.Doclever.is_text_present('用户名或者密码错误'))

    def tearDown(self):
        self.Doclever.close_driver()

if __name__ == "__main__":
    unittest.main()