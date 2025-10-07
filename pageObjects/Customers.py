from selenium.webdriver.common.by import By

class CustomersPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    ADD_NEW_BUTTON = (By.XPATH, "//a[contains(@href, '/Admin/Customer/Create') and contains(., 'Add new')]")
    SEARCH_EMAIL = (By.ID, "SearchEmail")
    SEARCH_FIRST_NAME = (By.ID, "SearchFirstName")
    SEARCH_LAST_NAME = (By.ID, "SearchLastName")
    SEARCH_BUTTON = (By.ID, "search-customers")
    SUCCESS_MESSAGE = (By.XPATH, "//*[contains(text(), 'The new customer has been added successfully') or contains(@class, 'alert-success')]")
    CUSTOMERS_TABLE = (By.ID, "customers-grid")
    NO_DATA_MESSAGE = (By.XPATH, "//*[contains(text(),'No data available in table')]")

    # Locator for success notification/banner
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'alert-success') or contains(text(),'The new customer has been added successfully')]")

    # Actions
    def click_add_new(self):
        self.driver.find_element(*self.ADD_NEW_BUTTON).click()

    def click_search(self):
        self.driver.find_element(*self.SEARCH_BUTTON).click()

    def get_success_message_text(self):
        return self.driver.find_element(*self.SUCCESS_MESSAGE).text

    def is_no_data_message_displayed(self):
        return len(self.driver.find_elements(*self.NO_DATA_MESSAGE)) > 0

    def get_customers_table(self):
        return self.driver.find_element(*self.CUSTOMERS_TABLE)

    # Utility: Combine search workflow
    def search_customer(self, email=None, first_name=None, last_name=None):
        if email:
            element = self.driver.find_element(*self.SEARCH_EMAIL)
            element.clear()
            element.send_keys(email)
        if first_name:
            element = self.driver.find_element(*self.SEARCH_FIRST_NAME)
            element.clear()
            element.send_keys(first_name)
        if last_name:
            element = self.driver.find_element(*self.SEARCH_LAST_NAME)
            element.clear()
            element.send_keys(last_name)
        self.click_search()

    def get_success_message_text(self):
        return self.driver.find_element(*self.SUCCESS_MESSAGE).text
