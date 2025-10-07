import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.Customers import CustomersPage
from pageObjects.AddCustomer import AddNewCustomerPage

from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.excelUtils import get_login_data
from selenium.webdriver.common.by import By
import os
import datetime

baseURL = ReadConfig.geturl()
email = ReadConfig.getemail()
password = ReadConfig.getpassword()

logger = LogGen.loggen()  # Named logger

def flush_logger():
    for handler in logger.handlers:
        handler.flush()

class TestAddCustomer:
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_addCustomer(self, driver):
        logger.info(f"********** started TestAddCustomer: test_login **********")
        flush_logger()
        driver.get(baseURL)
        login_page = LoginPage(driver)
        login_page.set_username(email)
        login_page.set_password(password)
        login_page.click_login()
        logger.info(f"********** Login Success **********")
        logger.info(f"********** Start Adding Customer **********")

        # Add customer steps
        customer_page = CustomersPage(driver)
        add_customer_page = AddNewCustomerPage(driver)

        add_customer_page.click_customer_menu()
        add_customer_page.click_customers_submenu()

        customer_page.click_add_new()

        # Generate a unique email for each test run
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        unique_email = f"testuser_{timestamp}@example.com"
        add_customer_page.enter_email(unique_email)
        add_customer_page.enter_password("Test@1234")
        add_customer_page.enter_first_name("Test")
        add_customer_page.enter_last_name("User")
        add_customer_page.select_gender("Male")
        add_customer_page.enter_company_name("Test Company")
        add_customer_page.set_tax_exempt(False)
        add_customer_page.set_active(True)
        add_customer_page.enter_admin_comment("Added by automation script.")
        add_customer_page.click_save()
        logger.info(f"********** Customer Added **********")
        # Validate success message
        success_message = customer_page.get_success_message_text()
        assert "The new customer has been added successfully" in success_message, (
            f"Expected success message not found. Actual: {success_message}")
        logger.info(f"********** Success message validated: {success_message} **********")
        flush_logger()
