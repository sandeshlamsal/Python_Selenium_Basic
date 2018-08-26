from selenium import webdriver
import unittest

#define class
#TestCase is a class
class Test_Selenium(unittest.TestCase):

    #add this anotation to run the setupClass and teardownClass
    @classmethod
    def setUpClass(cls):
        print("Run Once Class")

    def test_method1(self):
        print("Running Method1")

    def test_method2(self):
        print("Running Method2")

    # this must be added, self here is current class
    @classmethod
    def tearDownClass(self):
        print("Run once in a class")


#to run the test
if __name__=='__main__':
    unittest.main(verbosity=2)  # will get info of output running