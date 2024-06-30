import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise")

#Dynamic dropdowns
driver.find_element(By.ID, "autosuggest").send_keys("IND")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class = 'ui-menu-item'] a")
print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break

time.sleep(2)
#get attribute of current values
print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"
driver.quit()

#dynamic checkbox

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements(By.XPATH, "//input[@type ='checkbox']")
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        break


radio_buttons = driver.find_elements(By.XPATH,"//input[@type ='radio']")
for radio in radio_buttons:
    if radio.get_attribute('value') == 'radio2':
        radio.click()
        break


# alerts
driver.find_element(By.ID,"name").send_keys("Sam")
driver.find_element(By.ID, "alertbtn").click()
alert1 = driver.switch_to.alert
print(alert1.text)
alert1.accept()   #this will accept the message on the alert popup(java script)
# alert1.dismiss()  #this will reject the message on the alert popup



