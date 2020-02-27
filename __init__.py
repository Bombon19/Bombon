from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
print("Hello Python")

driver = webdriver.Chrome("C:\chromedriver.exe")
driver.get("https://lkmdemoaut.accenture.com/TestMeApp/RegisterUser.htm")
time.sleep(5)
driver.find_element_by_name('userName').send_keys("Leo10")
driver.find_element_by_id('firstName').send_keys("Leo")
driver.find_element_by_name('lastName').send_keys('Messi')
driver.find_element_by_xpath("//input[@value='Male']").click()
driver.find_element_by_xpath("//img[@alt='Ch']").click()
select  = Select(driver.find_element_by_xpath("//select[@data-handler='selectMonth']"))
select.select_by_visible_text('May')

select1  = Select(driver.find_element_by_xpath("//select[@data-handler='selectYear']"))
select1.select_by_visible_text('1993')

driver.find_element_by_xpath("//a[contains(.,'28')]").click()

time.sleep(2)

#select.select_by_value('411012')
#driver.find_element_by_name('btnK').click()
