import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.AddCustomer import AddNewCustomerPage
from pageObjects.LoginPage import LoginPage
from pageObjects.Customers import CustomersPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

baseURL = ReadConfig.geturl()
email = ReadConfig.getemail()
password = ReadConfig.getpassword()

logger = LogGen.loggen()  # Named logger

def flush_logger():
    for handler in logger.handlers:
        handler.flush()

class TestCustomerSearch:
    @pytest.mark.parametrize("search_email,should_exist",
                            [("steve_gates@nopCommerce.com", True),("nonexistentuser@example.com", False)])
    def test_search_customer_by_email(self, driver, search_email, should_exist):
        logger.info(f"********** started TestCustomerSearch: test_search_customer_by_email for {search_email} **********")
        flush_logger()
        driver.get(baseURL)
        login_page = LoginPage(driver)
        login_page.set_username(email)
        login_page.set_password(password)
        login_page.click_login()
        logger.info(f"********** Login Success **********")

        # Navigate to Customers page
        add_customer_page = AddNewCustomerPage(driver)
        add_customer_page.click_customer_menu()
        add_customer_page.click_customers_submenu()

        # Use the cleaner utility method for searching
        customers_page = CustomersPage(driver)
        customers_page.search_customer(email=search_email)

        # Explicit wait for table to update (wait for at least one row or 'no data' message)
        WebDriverWait(driver, 10).until(
            lambda d: len(customers_page.get_customers_table().find_elements(By.TAG_NAME, "tr")) > 1 or customers_page.is_no_data_message_displayed()
        )

        if should_exist:
            # Fetch the table and rows after the wait to ensure fresh elements (avoid stale elements)
            table = customers_page.get_customers_table()
            rows = table.find_elements(By.TAG_NAME, "tr")
            found = False #Flag to indicate if email was found

            for row in rows:
                if search_email in row.text:
                    found = True
                    break
            assert found, f"Customer with email {search_email} should exist but was not found in the table."
        else:
            assert customers_page.is_no_data_message_displayed(), f"Customer with email {search_email} should NOT exist, but table is not empty."
        logger.info(f"********** completed TestCustomerSearch: test_search_customer_by_email for {search_email} **********")
        flush_logger()
