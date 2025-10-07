import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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
         [
          ("steve_gates@nopCommerce.com", True),("nonexistentuser@example.com", False)
          #("steve_gates@nopCommerce.com", True)
         ])

    # Test searching multiple customers/each email treated as separate test to ensure fresh state.
    # Browser closes and navigation happens for each test
    def test001_search_customer_by_email(self, driver, search_email, should_exist):
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

        # Use utility method for searching by email
        customers_page = CustomersPage(driver)
        customers_page.search_customer(email=search_email)

        # Explicit wait for table to update (wait for at least one row or 'no data' message)
        WebDriverWait(driver, 10).until(
            lambda d: len(customers_page.get_customers_table().find_elements(By.TAG_NAME, "tr")) > 1 or customers_page.is_no_data_message_displayed()
        )
        time.sleep(2)
        found = False
        table = customers_page.get_customers_table()
        rows = table.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            try:
                if search_email in row.text:
                    found = True
                    break
            except Exception as e:
                logger.warning(f"Stale row encountered: {e}")
                continue
        if should_exist:
            assert found, f"Customer with email {search_email} should exist but was not found in the table."
        else:
            assert customers_page.is_no_data_message_displayed(), f"Customer with email {search_email} should NOT exist, but table is not empty."
        logger.info(f"********** completed TestCustomerSearch: test_search_customer_by_email for {search_email} **********")
        flush_logger()

    # Test searching multiple customers in one test without closing the BROWSER
    def test002_search_multiple_customers(self, driver):
        logger.info("********** started TestCustomerSearch: test_search_multiple_customers **********")
        flush_logger()
        driver.get(baseURL)
        login_page = LoginPage(driver)
        login_page.set_username(email)
        login_page.set_password(password)
        login_page.click_login()
        logger.info("********** Login Success **********")

        # Navigate to Customers page
        add_customer_page = AddNewCustomerPage(driver)
        add_customer_page.click_customer_menu()
        add_customer_page.click_customers_submenu()

        customers_page = CustomersPage(driver)
        test_data = [
            ("steve_gates@nopCommerce.com", True),
            ("nonexistentuser@example.com", False)
        ]
        for search_email, should_exist in test_data:
            customers_page.search_customer(email=search_email)
            WebDriverWait(driver, 10).until(
                lambda d: len(customers_page.get_customers_table().find_elements(By.TAG_NAME, "tr")) > 1 or customers_page.is_no_data_message_displayed()
            )
            time.sleep(2)
            found = False
            table = customers_page.get_customers_table()
            rows = table.find_elements(By.TAG_NAME, "tr")
            for row in rows:
                try:
                    if search_email in row.text:
                        found = True
                        break
                except Exception as e:
                    logger.warning(f"Stale row encountered: {e}")
                    continue
            if should_exist:
                assert found, f"Customer with email {search_email} should exist but was not found in the table."
            else:
                assert customers_page.is_no_data_message_displayed(), f"Customer with email {search_email} should NOT exist, but table is not empty."
            logger.info(f"Checked search for {search_email} (should_exist={should_exist})")
            # Optionally clear the search field if your page requires it
            # customers_page.clear_search_fields()  # Implement this if needed
        logger.info("********** completed TestCustomerSearch: test_search_multiple_customers **********")
        flush_logger()

    @pytest.mark.parametrize("first_name,last_name,should_exist",
         [
          ("Steve", "Gates", True),("Nonexistent", "User", False)
         ])
    def test003_search_customer_by_first_last_name(self, driver, first_name, last_name, should_exist):
        logger.info(f"********** started TestCustomerSearch: test_search_customer_by_first_last_name for {first_name} {last_name} **********")
        flush_logger()
        driver.get(baseURL)
        login_page = LoginPage(driver)
        login_page.set_username(email)
        login_page.set_password(password)
        login_page.click_login()
        logger.info(f"********** Login Success **********")
        add_customer_page = AddNewCustomerPage(driver)
        add_customer_page.click_customer_menu()
        add_customer_page.click_customers_submenu()
        customers_page = CustomersPage(driver)
        customers_page.search_customer(first_name=first_name, last_name=last_name)
        WebDriverWait(driver, 10).until(
            lambda d: len(customers_page.get_customers_table().find_elements(By.TAG_NAME, "tr")) > 1 or customers_page.is_no_data_message_displayed()
        )
        time.sleep(2)
        found = False
        table = customers_page.get_customers_table()
        rows = table.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            try:
                if first_name in row.text and last_name in row.text:
                    found = True
                    break
            except Exception as e:
                logger.warning(f"Stale row encountered: {e}")
                continue
        if should_exist:
            assert found, f"Customer with name {first_name} {last_name} should exist but was not found in the table."
        else:
            assert customers_page.is_no_data_message_displayed(), f"Customer with name {first_name} {last_name} should NOT exist, but table is not empty."
        logger.info(f"********** completed TestCustomerSearch: test_search_customer_by_first_last_name for {first_name} {last_name} **********")
        flush_logger()