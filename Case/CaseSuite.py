import unittest

from HtmlTestRunner import HTMLTestRunner

from Case.Case_1 import DoTestCase

suite = unittest.TestSuite()
tests = [DoTestCase('test_1'),DoTestCase('test_2')]
suite.addTests(tests)
runner = HTMLTestRunner()
runner.run(suite)