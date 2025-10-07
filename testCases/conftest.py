import pytest
from selenium import webdriver
import os

@pytest.fixture()
def driver(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  # waits up to 10 seconds for elements to appear
    request.node.driver = driver  # Attach driver to the test node for access in hooks
    yield driver  # <-- gives driver to the test
    driver.quit()  # <-- runs after the test, closes browser


def pytest_runtest_makereport(item, call):
    if call.when == 'call' and call.excinfo is not None:
        driver = getattr(item, 'driver', None)
        if driver:
            screenshots_dir = os.path.join(os.path.dirname(item.fspath), '../screenshots')
            os.makedirs(screenshots_dir, exist_ok=True)
            test_name = item.name.replace(':', '_').replace('/', '_')
            screenshot_path = os.path.join(screenshots_dir, f'{test_name}.png')
            driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved to {screenshot_path}")
