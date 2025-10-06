import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage

class TestLoginPage:
    def test_login_page_title(self, driver):
        driver.get("https://admin-demo.nopcommerce.com")
        print(f"Page title is: {driver.title}")  # Log the title
        assert driver.title == "nopCommerce demo store. Logi", "Title does not match!"

    def test_login(self, driver):
        driver.get("https://admin-demo.nopcommerce.com")
        login_page = LoginPage(driver)
        login_page.set_username("admin@yourstore.com")
        login_page.set_password("admin")
        login_page.click_login()

        # assert login_page.is_logo_present(), "Login failed or logo not present after login."
        assert login_page.is_gearicon_present(), "Login failed as Gear Icon not present after login"