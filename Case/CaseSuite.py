import unittest

from HtmlTestRunner import HTMLTestRunner

from Case.Case_1 import DoTestCase

suite = unittest.TestSuite()
tests = [DoTestCase('test_login')]
suite.addTests(tests)
runner = HTMLTestRunner(output='./reports')
runner.run(suite)