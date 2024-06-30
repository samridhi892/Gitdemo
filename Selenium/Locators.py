import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

url = "https://rahulshettyacademy.com/angularpractice/"
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Samridhi Pradhan")
driver.find_element(By.NAME, "email").send_keys("sp@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("12345")
driver.find_element(By.XPATH,"//input[@id='exampleCheck1']").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()

#Static Dropdowns
driver1 = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
driver1.select_by_index(1)
driver1.select_by_visible_text("Male")

#Radio Button
driver.find_element(By.XPATH,"//input[@id='inlineRadio2']")

message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message





time.sleep(3)
