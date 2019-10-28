import datetime

from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path = 'drivers/chromedriver')

driver.get("https://jobs.apple.com/en-us/search?sort=relevance")

driver.maximize_window()

#//div[@class='accordion-icon icon icon-after icon-plus']

searchFilters = driver.find_elements_by_xpath("//div[@class='accordion-icon icon icon-after icon-plus']")

for filters in searchFilters:
    driver.execute_script("arguments[0].click();", filters)
    time.sleep(2)

#Filter via Location
driver.find_element_by_xpath("//input[@id='locations-filter-input']").send_keys("ch")
time.sleep(2)
suggestedLocations = driver.find_elements_by_xpath("//li[contains(@id,'locations-filter-input-option')]")
suggestedLocations[3].click()

#Filter via keyword
time.sleep(2)
driver.find_element_by_xpath("//input[@id='keywords-filter-input']").send_keys("CN")

#Filter via Teams
time.sleep(2)
driver.find_element_by_xpath("//input[@id='teams-filter-input']").send_keys("Retail")
time.sleep(2)
suggestedTeams = driver.find_elements_by_xpath("//li[contains(@id,'teams-filter-input-option')]")
suggestedTeams[1].click()

#Filter via Products and services
time.sleep(2)
driver.find_element_by_xpath("//button[contains(text(),'More')]").click()
time.sleep(2)
productList = driver.find_elements_by_xpath("//span[contains(@class,'products-and-services-filter-checklist')]")
for product in productList:
    driver.execute_script("arguments[0].click();", product)
    time.sleep(1)

#filter via Language Skills
time.sleep(2)
driver.find_element_by_xpath("//input[@id='languages-filter-input']").send_keys("ch")
time.sleep(2)
suggestedTeams = driver.find_elements_by_xpath("//li[contains(@id,'languages-filter-input-option')]")
suggestedTeams[4].click()

#Screenshot

#(MonthName+Day_12Hour:Minute+AM/PM)

now = datetime.datetime.now().strftime("%B%d_%I:%M%p")

driver.save_screenshot('screenshots/' + now + '.png')






