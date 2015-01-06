'''
Created on 02-Jan-2015

@author: naveen
'''
'''''from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.get("https://www.google.co.in/?gws_rd=ssl")
#assert "Python" in driver.title
elem = driver.find_element_by_xpath(".//*[@id='gb']/div[1]/div[1]/div[1]/div[2]/a").click()
driver.maximize_window()
driver.save_screenshot('/home/naveen/Desktop/output/screenshot.png')
elem = driver.find_element_by_xpath(".//*[@id='Email']").send_keys("navdheep")
elem = driver.find_element_by_xpath(".//*[@id='Passwd']").send_keys("naveen@111")
elem = driver.find_element_by_xpath(".//*[@id='signIn']").click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
element = WebDriverWait(driver, 10)
elem = driver.back()

#elem = driver.find_element_by_name("q")
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source

driver.close()'''''

from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.python.org/')
driver.set_window_size(600, 600, 1)

