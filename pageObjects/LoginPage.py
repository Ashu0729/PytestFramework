from selenium.webdriver.common.by import By


class LoginPage:
    # Locators
    USERNAME_INPUT  = (By.ID, "Email")
    PASSWORD_INPUT = (By.ID, "Password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    LOGO = (By.XPATH, "//img[@alt='nopCommerce admin logo']")
    GEAR_ICON = (By.CSS_SELECTOR, "i.fas.fa-gears")
    ERROR_MESSAGE = (By.XPATH, "//div[contains(@class, 'message-error')]")
    LOGOUT = (By.LINK_TEXT, "Logout")

    def __init__(self, driver):
        self.driver = driver

    # Page Actions  Methods
    def set_username(self, username):
        self.driver.find_element(*self.USERNAME_INPUT).clear()
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def is_logo_present(self):
        return self.driver.find_element(*self.LOGO).is_displayed()

    def is_gearicon_present(self):
        return self.driver.find_element(*self.GEAR_ICON).is_displayed()