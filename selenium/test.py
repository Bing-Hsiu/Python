import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#browser = webdriver.Chrome('/Users/binshu/Desktop/chromedriver')
browser = webdriver.Safari()
browser.get("http://www.google.com")
#time.sleep(10)

search = browser.find_element_by_name('q')
search.send_keys('ChromeDriver')
search.submit()
#time.sleep(10)
browser.quit()             
