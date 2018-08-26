from selenium import webdriver
import unittest

#define class
#TestCase is a class
class Test_Selenium(unittest.TestCase):
    def setUp(self):
        print("Run before every test")

    def test_method1(self):
        print("Running Method1")

    def test_method2(self):
        print("Running Method2")

    def tearDown(self):
        print("Run After every Test")


#to run the test
if __name__=='__main__':
    unittest.main(verbosity=2)  # will get info of output running