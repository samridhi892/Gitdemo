import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.LINK_TEXT, "Shop").click()

products = driver.find_elements(By.XPATH, "//div[@class = 'card h-100']")

for product in products:
    product_name = product.find_element(By.XPATH, "div/h4/a").text
    if product_name == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()
        break

driver.find_element(By.PARTIAL_LINK_TEXT,"Checkout").click()
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("IND")
wait = WebDriverWait(driver,10)
wait.until(ec.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT,"India").click()

driver.find_element(By.XPATH,"//label[@for ='checkbox2']").click()
driver.find_element(By.XPATH,"//input[@value ='Purchase']").click()

message = driver.find_element(By.XPATH,"//div[@class ='alert alert-success alert-dismissible']").text
print(message)
assert 'Success! Thank you! ' in message



time.sleep(4)
