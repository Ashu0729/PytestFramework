import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.excelUtils import get_login_data
import os

baseURL = ReadConfig.geturl()

logger = LogGen.loggen()  # Named logger

def flush_logger():
    for handler in logger.handlers:
        handler.flush()

# Path to the Excel file
excel_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'TestData', 'LoginData.xlsx')
# Specify the sheet name explicitly
login_data = get_login_data(excel_path, sheet_name="Sheet1")

class TestLoginPageDataDriven:
    @pytest.mark.parametrize("username,password,exp", login_data)
    @pytest.mark.regression
    def test_valid_login(self, driver, username, password, exp):
        logger.info(f"********** started TestLoginPage: test_login with {username} **********")
        flush_logger()
        driver.get(baseURL)
        login_page = LoginPage(driver)
        login_page.set_username(username)
        login_page.set_password(password)
        login_page.click_login()
        login_success = login_page.is_gearicon_present()

        if exp.lower() == "pass":
            assert login_success, f"Expected login to succeed for user {username}, but it failed."
        else:
            assert not login_success, f"Expected login to fail for user {username}, but it succeeded."
        logger.info(f"********** ending TestLoginPage: test_login with {username} **********")
        flush_logger()
