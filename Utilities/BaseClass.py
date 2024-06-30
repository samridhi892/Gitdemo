import pytest
import logging
from selenium import webdriver
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:
    driver: webdriver

    def select_option_by_text(self, locator, text):
        driver1 = Select(locator)
        driver1.select_by_visible_text(text)

    def get_logging(self):
        logger = logging.getLogger(__name__)

        filehandle = logging.FileHandler("file_log.log")  # declaring the file name when the logs will be placed
        formater = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")  # format of the log file
        filehandle.setFormatter(formater)
        logger.addHandler(filehandle)
        logger.setLevel(logging.DEBUG)
        return logger
        # logger.debug("A debug statement is executed")
        # logger.info("Information statement")
        # logger.warning("Warning mode ")
        # logger.error("A major error has happened")
        # logger.critical("Critical issue")
