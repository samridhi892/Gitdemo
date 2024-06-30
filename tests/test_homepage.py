import pytest
from selenium.webdriver.support.select import Select

from PageObjectModel.HomePage import HomePage
from TestData.HomePageData import HomePageData
from Utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_form_submission(self, getdata):
        log = self.get_logging()
        homepage = HomePage(self.driver)

        log.info("entering the first name" + getdata["Name"])
        homepage.get_name().send_keys(getdata["Name"])
        log.info("entering the email")
        homepage.get_email().send_keys(getdata["Email"])
        homepage.get_password().send_keys("123")
        homepage.get_checkbox().click()
        homepage.submit_button().click()


        # Static Dropdowns
        self.select_option_by_text(homepage.get_gender(), getdata["Gender"])

        # Radio Button
        homepage.radio_button().click()

        log.info("the message")
        message = homepage.get_message().text
        log.info(message)
        log.info("checking message is correct")
        assert "Success" in message
        self.driver.refresh()

    # @pytest.fixture(params=[("Samridhi", "sp@gmail.com", "Female"), ("Vivek", "vp@gmail.com", "Male")])
    # def getdata(self, request):
    #     return request.param

    @pytest.fixture(params=HomePageData.getTestData("test case2"))
    def getdata(self, request):
        return request.param
