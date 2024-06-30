from selenium.webdriver.common.by import By

from PageObjectModel.Checkout import Checkout


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.LINK_TEXT, "Shop")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.XPATH, "//input[@id='exampleCheck1']")
    submit = (By.XPATH, "//input[@type='submit']")
    radio = (By.XPATH, "//input[@id='inlineRadio2']")
    message = (By.CLASS_NAME, "alert-success")
    gender = (By.ID, "exampleFormControlSelect1")
    def shopitem(self):
        self.driver.find_element(*HomePage.shop).click()
        checkout = Checkout(self.driver)
        return checkout

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_email(self):
        return self.driver.find_element(*HomePage.email)

    def get_password(self):
        return self.driver.find_element(*HomePage.password)

    def get_checkbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def submit_button(self):
        return self.driver.find_element(*HomePage.submit)

    def radio_button(self):
        return self.driver.find_element(*HomePage.radio)

    def get_message(self):
        return self.driver.find_element(*HomePage.message)

    def get_gender(self):
        return self.driver.find_element(*HomePage.gender)
