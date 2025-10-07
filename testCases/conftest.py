import pytest
from selenium import webdriver
import os

# Pytest hook to add command line option for browser choice
def pytest_addoption(parser):
    parser.addoption("--browser",
                    action="store",
                    default="chrome",
                    help="Browser to run tests against: chrome, firefox, edge"
    )

@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser").lower()
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching Chrome browser...")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox browser...")
    elif browser == "edge":
        driver = webdriver.Edge()
        print("Launching Edge browser...")
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.implicitly_wait(10)  # waits up to 10 seconds for elements to appear
    request.node.driver = driver  # Attach driver to the test node for access in hooks
    yield driver  # <-- gives driver to the test
    driver.quit()  # <-- runs after the test, closes browser

#Pytest Hook for Screenshot - runs custom code after each test phase (setup, call, teardown)
# and inspect the result of the test
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

# Pytest Hook for HTML Reports
def pytest_configure(config):
    # Ensure Reports directory exists
    reports_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Reports'))
    os.makedirs(reports_dir, exist_ok=True)

# Custom HTML report title
def pytest_html_report_title(report):
    report.title = "nopCommerce Automation Test Report"

# Add custom metadata to HTML report summary
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([
        "Project Name: nopCommerce",
        "Module Name: Customers",
        "Tester: Ashutosh"
    ])