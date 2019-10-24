import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path = 'drivers/chromedriver')
driver.get("http://newtours.demoaut.com/mercurysignon.php")
driver.maximize_window()

driver.find_element_by_xpath("//input[@name='userName']").send_keys("mercury")
driver.find_element_by_xpath("//input[@name='password']").send_keys("mercury")
driver.find_element_by_xpath("//input[@name='login']").click()

time.sleep(2)

driver.find_element_by_xpath("//input[@name='tripType' and @value='oneway']").click()

passengerCount = Select(driver.find_element_by_xpath("//select[@name='passCount']"))
passengerCount.select_by_value("2")

fromPort = Select(driver.find_element_by_xpath("//select[@name='fromPort']"))
fromPort.select_by_value("New York")

fromMonth = Select(driver.find_element_by_xpath("//select[@name='fromMonth']"))
fromMonth.select_by_visible_text("January")

fromDay = Select(driver.find_element_by_xpath("//select[@name='fromDay']"))
fromDay.select_by_value("1")

toPort = Select(driver.find_element_by_xpath("//select[@name='toPort']"))
toPort.select_by_value("Sydney")

toMonth = Select(driver.find_element_by_xpath("//select[@name='toMonth']"))
toMonth.select_by_visible_text("December")

toDay = Select(driver.find_element_by_xpath("//select[@name='toDay']"))
toDay.select_by_value("30")

driver.find_element_by_xpath("//input[@name='servClass' and @value='First']").click()

airline = Select(driver.find_element_by_xpath("//select[@name='airline']"))
airline.select_by_visible_text("Pangea Airlines")

driver.find_element_by_xpath("//input[@name='findFlights']").click()
