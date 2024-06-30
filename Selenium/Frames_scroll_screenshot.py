import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certification-errors")

driver = webdriver.Chrome(options=chrome_options)

driver.maximize_window()
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# driver.switch_to.frame("courses-iframe")
# driver.find_element(By.LINK_TEXT,"Courses").click()
# time.sleep(5)

driver.execute_script("window.scroll(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("screenshot1.png")
time.sleep(2)

action = ActionChains(driver)

driver.forward()

