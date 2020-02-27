import time
print("hello Python")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from select import select
from selenium.webdriver.support.select import Select


driver= webdriver.Chrome("C:\chromedriver.exe")
driver.get("https://lkmdemoaut.accenture.com/TestMeApp/RegisterUser.htm")
driver.find_element_by_name("userName").send_keys("Leo10")
driver.find_element_by_name("firstName").send_keys("Leo")
driver.find_element_by_name("lastName").send_keys("Messi")
driver.find_element_by_name("Password").send_keys("paithon")
driver.find_element_by_xpath("//input[@value= 'Male']").click()
select = Select(driver.find_element_by_name('securityQuestion'))

select.select_by_visible_text('What is your favourite colour?')
time.sleep(2)
select.select_by_value('411002')