import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

baseURL = ReadConfig.geturl()
email = ReadConfig.getemail()
password = ReadConfig.getpassword()

logger = LogGen.loggen()  # Named logger

def flush_logger():
    for handler in logger.handlers:
        handler.flush()

class TestLoginPage:
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_login_page_title(self, driver):
        logger.info("********** started TestLoginPage: test_login_page_title **********")
        flush_logger()
        driver.get(baseURL)
        print(f"Page title is: {driver.title}")  # Log the title
        assert driver.title == "nopCommerce demo store. Login", "Title does not match!"
        logger.info("********** ending TestLoginPage: test_login_page_title **********")
        flush_logger()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_login(self, driver):
        logger.info("********** started TestLoginPage: test_login **********")
        flush_logger()
        driver.get(baseURL)
        login_page = LoginPage(driver)
        login_page.set_username(email)
        login_page.set_password(password)
        login_page.click_login()
        assert login_page.is_gearicon_present(), "Login failed as Gear Icon not present after login"
        logger.info("********** ending TestLoginPage: test_login **********")
        flush_logger()
