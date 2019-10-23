import time
from selenium import webdriver

driver = webdriver.Chrome('drivers/chromedriver')

driver.get("http://newtours.demoaut.com/")

driver.find_element_by_xpath("//input[@name='userName']").send_keys("jserra")

driver.find_element_by_xpath("//input[@name='password']").send_keys("p@ssword")

driver.find_element_by_xpath("//input[@name='login']").click()

time.sleep(5)

driver.quit()




