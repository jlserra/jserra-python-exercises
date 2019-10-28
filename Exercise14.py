from selenium import webdriver

driver = webdriver.Chrome(executable_path = 'drivers/chromedriver')

driver.get("https://chercher.tech/practice/frames-example-selenium-webdriver")
driver.maximize_window()

#Step 1
driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='frame1']"))
driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='frame3']"))
driver.find_element_by_xpath("//input[@id='a']").click()

#Step 2
driver.switch_to.default_content( )
driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='frame1']"))
driver.find_element_by_xpath("//input[@type='text']").send_keys("Selenium")

#Step 3
driver.switch_to.default_content( )
isValid = driver.find_element_by_xpath("//span[contains(text(),'Not a Friendly Topic')]").text != "selenium Webdriver"
print "text is not equal to selenium webdriver", isValid


