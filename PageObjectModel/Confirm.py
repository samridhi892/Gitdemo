from selenium.webdriver.common.by import By


class Confirm:

    success_button = (By.XPATH, "//button[@class='btn btn-success']")
    country_selection = (By.XPATH, "//input[@type='text']")
    checkbox = (By.XPATH, "//label[@for ='checkbox2']")
    purchase = (By.XPATH, "//input[@value ='Purchase']")
    message = (By.XPATH, "//div[@class ='alert alert-success alert-dismissible']")

    def __init__(self,driver):
        self.driver =driver

    def successbtn(self):
        self.driver.find_element(Confirm.success_button)

    def country(self):
        self.driver.find_element(Confirm.country_selection)



    def checkbox(self):
        self.driver.find_element(Confirm.checkbox)

    def purchase(self):
        self.driver.find_element(Confirm.purchase)

    def message(self):
        self.driver.find_element(Confirm.message)

