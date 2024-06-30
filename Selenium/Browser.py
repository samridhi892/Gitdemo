import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com")
# driver.get("https://login.veevavault.com/")
driver.maximize_window()
print(driver.title)    #-->this will get the title of the browser page
print(driver.current_url)  #--->get the current url of the page






time.sleep(5)