from selenium.webdriver.common.by import By


class Checkout:
    products = (By.XPATH, "//div[@class = 'card h-100']")
    check_out_button = (By.PARTIAL_LINK_TEXT, "Checkout")

    def __init__(self, driver):
        self.driver = driver

    def get_product(self):
        return self.driver.find_elements(Checkout.products)

    def checkout_button(self):
        return self.driver.find_element(Checkout.check_out_button)
