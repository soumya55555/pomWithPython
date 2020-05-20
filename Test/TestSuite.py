import unittest
from Test.LoginTest import LoginTest
from Test.ProductsTest import ProductsTest


tc1=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2=unittest.TestLoader().loadTestsFromTestCase(ProductsTest)

masterTestSuite=unittest.TestSuite([tc2])

unittest.TextTestRunner().run(masterTestSuite)