import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  # waits up to 10 seconds for elements to appear
    yield driver  # <-- gives driver to the test
    driver.quit()  # <-- runs after the test, closes browser
