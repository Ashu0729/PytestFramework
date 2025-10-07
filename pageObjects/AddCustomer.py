from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddNewCustomerPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators

    # Locators for left navigation
    CUSTOMER_MENU = (By.XPATH, "(//p[normalize-space()='Customers']/parent::a)[1]")
    CUSTOMERS_SUBMENU = (By.XPATH, "(//p[normalize-space()='Customers'])[2]")

    # Locator for the "Add new" button (robust: href and text)
    #ADD_NEW_BUTTON = (By.XPATH, "//a[contains(@href, '/Admin/Customer/Create') and normalize-space()='Add new']")

    # Locators for the Add New Customer form fields
    EMAIL = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")
    FIRST_NAME = (By.ID, "FirstName")
    LAST_NAME = (By.ID, "LastName")
    GENDER_MALE = (By.ID, "Gender_Male")
    GENDER_FEMALE = (By.ID, "Gender_Female")
    COMPANY_NAME = (By.ID, "Company")
    IS_TAX_EXEMPT = (By.ID, "IsTaxExempt")
    NEWSLETTER = (By.XPATH, "//input[contains(@aria-label, 'Newsletter')]")
    CUSTOMER_ROLES = (By.XPATH, "//select[contains(@aria-haspopup, 'menu')]")
    MANAGER_VENDOR = (By.XPATH, "//select[@aria-label='Manager of vendor']")
    ACTIVE = (By.ID, "Active")
    ADMIN_COMMENT = (By.ID, "AdminComment")
    SAVE_BUTTON = (By.NAME, "save")
    SAVE_CONTINUE_BUTTON = (By.NAME, "save-continue")
    CANCEL_BUTTON = (By.XPATH, "//a[contains(@href, '/Admin/Customer/List')]")


    # Methods
    def click_customer_menu(self):
        self.driver.find_element(*self.CUSTOMER_MENU).click()

    def click_customers_submenu(self):
        self.driver.find_element(*self.CUSTOMERS_SUBMENU).click()

    def click_add_new(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.ADD_NEW_BUTTON)
        ).click()

    def enter_email(self, email):
        self.driver.find_element(*self.EMAIL).clear()
        self.driver.find_element(*self.EMAIL).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD).clear()
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def enter_first_name(self, fname):
        self.driver.find_element(*self.FIRST_NAME).clear()
        self.driver.find_element(*self.FIRST_NAME).send_keys(fname)

    def enter_last_name(self, lname):
        self.driver.find_element(*self.LAST_NAME).clear()
        self.driver.find_element(*self.LAST_NAME).send_keys(lname)

    def select_gender(self, gender):
        if gender.lower() == 'male':
            self.driver.find_element(*self.GENDER_MALE).click()
        elif gender.lower() == 'female':
            self.driver.find_element(*self.GENDER_FEMALE).click()

    def enter_company_name(self, company):
        self.driver.find_element(*self.COMPANY_NAME).clear()
        self.driver.find_element(*self.COMPANY_NAME).send_keys(company)

    def set_tax_exempt(self, tax_exempt=True):
        checkbox = self.driver.find_element(*self.IS_TAX_EXEMPT)
        if checkbox.is_selected() != tax_exempt:
            checkbox.click()

    def set_active(self, active=True):
        checkbox = self.driver.find_element(*self.ACTIVE)
        if checkbox.is_selected() != active:
            checkbox.click()

    def enter_admin_comment(self, comment):
        self.driver.find_element(*self.ADMIN_COMMENT).clear()
        self.driver.find_element(*self.ADMIN_COMMENT).send_keys(comment)

    def click_save(self):
        self.driver.find_element(*self.SAVE_BUTTON).click()

    def click_save_continue(self):
        self.driver.find_element(*self.SAVE_CONTINUE_BUTTON).click()

    def click_cancel(self):
        self.driver.find_element(*self.CANCEL_BUTTON).click()


# Add methods for newsletter/customer roles/vendor fields as needed depending on test requirements.
