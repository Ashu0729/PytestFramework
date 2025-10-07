# PytestFramework

A robust and extensible automation framework built primarily using **Pytest** and **Selenium WebDriver**. This framework is designed for test automation of web applications with a focus on maintainability, advanced reporting, and ease of configuration.

---

## Key Features

### 1. **Cross-Browser & Configurable Test Execution**
- Easily select and configure the browser for test execution via command-line options.
- Supports integration with Selenium WebDriver for real browser automation.

### 2. **Modular Page Object Model**
- Encapsulates page-specific logic and locators via the Page Object Model design pattern for maintainable test scripts.

### 3. **Custom Test Data Management**
- Centralized management of test data through the `TestData` package, ensuring data-driven testing and easy scalability.

### 4. **Advanced Pytest Hooks & Fixtures**
- Custom `conftest.py` includes:
  - Browser setup/teardown as fixtures.
  - Hooks for customizing test runs, such as screenshot capture on failures, and dynamic HTML report enhancements.

### 5. **Rich HTML Reporting**
- Generates interactive and visually appealing HTML reports:
  - **Collapsible test result sections** for improved readability.
  - **Embedded media support**: Inline images and video (such as screenshots of failures or steps).
  - **Test logs**: Expandable log sections with error highlighting for rapid debugging.
  - **Environment summary**: Details Python version, OS, packages, plugins, and custom metadata.
  - **Filtering and sorting**: Filter results by status (passed, failed, skipped, etc.), and sort columns interactively.

### 6. **Custom Metadata & Reporting Enhancements**
- Add custom metadata to the HTML report summary using Pytest hooks.
- Custom HTML in reports via result table hooks.

### 7. **Interactive UI Elements in Reports**
- **Media carousel**: Browse multiple screenshots or videos per test.
- **Show/hide all details**: Quickly expand or collapse all test logs and media.
- **Dynamic filtering**: Checkbox-based filtering for results, with real-time updates.

### 8. **Extensible for Plugins**
- Integrates with popular Pytest plugins like `pytest-html`, `pytest-cov`, and `pytest-xdist` for parallel execution and coverage.

---

## Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ashu0729/PytestFramework.git
   cd PytestFramework
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run tests**

   **SingleTest in Edge**
   ```bash
   pytest -s -v --html=./Reports/report.html testCases/test_loginPage.py --browser=Edge
   ```
   **SanityTests in Chrome**
   ```bash
   pytest -s -v -m "sanity" --html=./Reports/report.html testCases --browser=Chrome
   ```
   **RegressionTests in Edge**
   ```bash
   pytest -s -v -m "regression" --html=./Reports/report.html testCases --browser=Edge
   ```
   **Run tests through Jenkins**
   ```bash
   call "C:\Users\ashut\PycharmProjects\Pytest Framework\.venv\Scripts\activate"
   pytest -s -v --html=./Reports/report.html testCases/test_loginPage.py --browser=Edge
   ```
---

## Directory Structure

- `testCases/` — Test scripts and fixtures (`conftest.py`)
- `pageObjects/` — Page Object Model classes
- `TestData/` — Centralized test data
- `Reports/` — Generated HTML reports and assets

---

## Tech Stack

- **Python** (Pytest, Selenium)
- **HTML, CSS, JavaScript** (for report generation and interactivity)

---

## Contributing

Contributions and suggestions are welcome! Please open issues or submit pull requests for improvements.

---

## License

This project is licensed under the MIT License.
