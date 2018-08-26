from selenium import webdriver

#define class
class Test_Selenium():

    #constructor call
    def Test_Selenium():
        driver = webdriver.Chrome("c://AutomationDriver//chromedriver")
        driver.get("https://www.facebook.com")

#call the class and run the program
obj_Test_Selenium=Test_Selenium()
obj_Test_Selenium.Test_Selenium()

