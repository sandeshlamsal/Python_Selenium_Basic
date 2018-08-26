from selenium import webdriver

driver = webdriver.Chrome("c://AutomationDriver//chromedriver")
driver.get("https://www.facebook.com")

email = driver.find_element_by_xpath("//input[@name='email']")
password = driver.find_element_by_xpath("//input[@name='pass']")
submit = driver.find_element_by_xpath("//input[@ value='Log In']")

email.send_keys("parasisandesh@yahoo.com")
password.send_keys("******")

submit.click()
driver.close()
driver.quit()
