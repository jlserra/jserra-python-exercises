import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

#driver = webdriver.Chrome('usr/bin/safaridriver')

driver = webdriver.Chrome(executable_path = 'drivers/chromedriver')
driver.get("http://newtours.demoaut.com/mercurysignon.php")
driver.maximize_window()
#Relative Xpath
driver.find_element_by_xpath("//input[@name='userName']").send_keys("mercury")
#Absolute Xpath
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/table[1]/tbody[1]/tr[4]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/table[1]/tbody[1]/tr[5]/td[1]/form[1]/table[1]/tbody[1]/tr[2]/td[2]/input[1]").send_keys("mercury")
#Contains
driver.find_element_by_xpath("//*[contains(@value,'Login')]").click()
time.sleep(2)
#AND
driver.find_element_by_xpath("//*[@name='tripType' and @value='oneway']").click()
#OR
driver.find_element_by_xpath("//*[@name='serv' or @value='Business']").click()
#Starts With
time.sleep(5)
driver.find_element_by_xpath("//*[starts-with(@name,'findF')]").click()
#driver.quit()
