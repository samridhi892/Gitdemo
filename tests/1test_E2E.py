import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from PageObjectModel.Checkout import Checkout
from PageObjectModel.Confirm import Confirm
from PageObjectModel.HomePage import HomePage
from Utilities.BaseClass import BaseClass


class Test_E2E(BaseClass):

    def test_e2e(self):

        homepage = HomePage(self.driver)
        checkout1 = homepage.shopitem()
        # checkout = Checkout(self.driver)
        products = checkout1.get_product()

        # self.driver.find_element(By.LINK_TEXT, "Shop").click()
        # products = self.driver.find_elements(By.XPATH, "//div[@class = 'card h-100']")
        #
        for product in products:
            product_name = product.find_element(By.XPATH, "div/h4/a").text
            if product_name == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()
                break

        checkout1.checkout_button().click()
        confirm_page = Confirm(self.driver)
        confirm_page.successbtn().click()
        confirm_page.country().send_keys("IND")



        # self.driver.find_element(By.PARTIAL_LINK_TEXT, "Checkout").click()
        # self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        # self.driver.find_element(By.XPATH, "//input[@type='text']").send_keys("IND")
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()

        confirm_page.checkbox().click()
        confirm_page.purchase().click()
        message = confirm_page.message().text
        # self.driver.find_element(By.XPATH, "//label[@for ='checkbox2']").click()
        # self.driver.find_element(By.XPATH, "//input[@value ='Purchase']").click()
        # message = self.driver.find_element(By.XPATH, "//div[@class ='alert alert-success alert-dismissible']").text
        print(message)
        assert 'Success! Thank you! ' in message
