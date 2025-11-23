# StyleZone Test Automation Framework

A comprehensive Selenium Python test automation framework for the StyleZone e-commerce application using Page Object Model (POM) pattern.

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running Tests](#running-tests)
- [Test Cases](#test-cases)
- [Configuration](#configuration)
- [Reports](#reports)
- [Best Practices](#best-practices)

## ✨ Features

- **Page Object Model (POM)**: Maintainable and reusable page objects
- **Pytest Framework**: Modern Python testing framework
- **Explicit Waits**: Robust element waiting strategies
- **Cross-browser Support**: Chrome WebDriver (extensible to other browsers)
- **HTML Reports**: Automatic test report generation
- **🐛 Bug Reports**: Automatic detailed bug reports on test failures (HTML, Markdown, JSON)
- **Screenshots**: Automatic screenshots on test failures
- **Test Markers**: Organized test execution with markers
- **Parallel Execution**: Support for parallel test execution
- **Live Application Testing**: Configured to test live application at https://muntasir101.github.io/stylezone

## 📁 Project Structure

```
StyleZoneAutomationTest/
├── locators/
│   └── locators.py              # All locator constants
├── pages/
│   ├── base_page.py             # Base page class with common methods
│   ├── home_page.py             # Home page object
│   └── shop_page.py             # Shop page object
├── tests/
│   ├── test_search.py           # Search functionality tests (TC-1 to TC-6, TC-15)
│   ├── test_sort_filter.py      # Sort and filter tests (TC-7 to TC-12)
│   ├── test_pagination.py       # Pagination tests (TC-13 to TC-14)
│   └── test_bug_report_demo.py  # Demo test for bug report generation
├── utils/
│   └── bug_report.py            # Bug report generator
├── bug_reports/                 # Generated bug reports (HTML, MD, JSON)
├── screenshots/                 # Screenshots on test failures
├── reports/                     # Test execution reports
├── conftest.py                  # Pytest fixtures and configuration
├── pytest.ini                   # Pytest configuration
├── config.py                    # Configuration settings
├── requirements.txt             # Python dependencies
├── run_tests.bat                # Windows test runner
├── run_tests.sh                 # Linux/Mac test runner
├── README_TEST_FRAMEWORK.md     # This file
├── BUG_REPORT_GUIDE.md          # Bug report documentation
├── QUICK_REFERENCE.md           # Quick command reference
└── FRAMEWORK_SUMMARY.md         # Framework summary
```

## 🔧 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Chrome browser installed
- Internet connection (for downloading ChromeDriver)

## 📦 Installation

1. **Clone or navigate to the project directory**

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Running Tests

### Run All Tests
```bash
pytest
```

### Run Tests by Marker
```bash
# Run only search tests
pytest -m search

# Run only sort tests
pytest -m sort

# Run only filter tests
pytest -m filter

# Run only pagination tests
pytest -m pagination

# Run smoke tests
pytest -m smoke

# Run regression tests
pytest -m regression
```

### Run Specific Test File
```bash
pytest tests/test_search.py
```

### Run Specific Test Case
```bash
pytest tests/test_search.py::TestSearchFunctionality::test_tc1_successful_search_partial_case_insensitive
```

### Run Tests in Parallel
```bash
pytest -n auto  # Uses all available CPU cores
pytest -n 4     # Uses 4 parallel workers
```

### Run with Verbose Output
```bash
pytest -v
```

### Run with HTML Report
```bash
pytest --html=reports/report.html --self-contained-html
```

## 📝 Test Cases

### Search Functionality Tests

| TC ID | Test Case | Status |
|-------|-----------|--------|
| TC-1 | Successful search (partial, case-insensitive) | ✅ |
| TC-2 | Exact match search | ✅ |
| TC-3 | No results found | ✅ |
| TC-4 | Empty search returns all products | ✅ |
| TC-5 | Query with special characters | ✅ |
| TC-6 | Long query truncation (>100 chars) | ✅ |
| TC-15 | Verify product display fields | ✅ |

### Sort and Filter Tests

| TC ID | Test Case | Status |
|-------|-----------|--------|
| TC-7 | Sort by price (Low → High) | ✅ |
| TC-8 | Sort by price (High → Low) | ✅ |
| TC-9 | Sort by name (A → Z) | ✅ |
| TC-10 | Filter by category | ✅ |
| TC-11 | Filter by price range | ✅ |
| TC-12 | Combine sorting and filtering | ✅ |

### Pagination Tests

| TC ID | Test Case | Status |
|-------|-----------|--------|
| TC-13 | Pagination – Next Page | ✅ |
| TC-14 | Pagination – Previous Page | ✅ |

## ⚙️ Configuration

### Environment Variables

Set these environment variables to customize test execution:

```bash
# Base URL (default: https://muntasir101.github.io/stylezone)
export BASE_URL="https://muntasir101.github.io/stylezone"

# Run in headless mode
export HEADLESS="true"

# Browser (future: chrome, firefox, edge)
export BROWSER="chrome"
```

### Pytest Configuration

Edit `pytest.ini` to customize:
- Test paths
- Markers
- Report options
- Output format

## 📊 Reports

### HTML Test Reports

HTML test reports are automatically generated in the `reports/` directory:

```bash
pytest --html=reports/report.html --self-contained-html
```

### 🐛 Bug Reports (Automatic)

**Bug reports are automatically generated when tests fail!**

Each failure generates detailed bug reports in three formats:

- **HTML Report** (`bug_reports/BUG_YYYYMMDD_HHMMSS.html`) - Beautiful, shareable format
- **Markdown Report** (`bug_reports/BUG_YYYYMMDD_HHMMSS.md`) - Text format for documentation
- **JSON Report** (`bug_reports/BUG_YYYYMMDD_HHMMSS.json`) - Machine-readable format

**What's included:**
- Test name and failure message
- Test steps (extracted from docstrings)
- Expected vs Actual results
- Screenshot (automatically captured)
- Environment information (browser, platform, URLs)
- Stack trace

**Example output:**
```
============================================================
BUG REPORT GENERATED
============================================================
Report ID: BUG_20251123_140537
Test: test_demo_failure_for_bug_report
HTML Report: bug_reports/BUG_20251123_140537.html
Markdown Report: bug_reports/BUG_20251123_140537.md
JSON Report: bug_reports/BUG_20251123_140537.json
============================================================
```

**Viewing Reports:**
- Open HTML files in any web browser for the best viewing experience
- Markdown files can be viewed in any text editor or markdown viewer
- JSON files can be parsed programmatically for integration

See [BUG_REPORT_GUIDE.md](BUG_REPORT_GUIDE.md) for complete documentation.

### Screenshots

Screenshots are automatically captured on test failures and saved in the `screenshots/` directory. They are also embedded in bug reports.

## 🎯 Best Practices

### 1. Locator Management
- All locators are centralized in `locators/locators.py`
- Use CSS selectors (preferred) or XPath when necessary
- IDs are preferred over classes for unique elements

### 2. Page Objects
- Each page has its own page object class
- Page objects inherit from `BasePage`
- Page objects contain all interactions with that page

### 3. Test Organization
- Tests are organized by functionality
- Use descriptive test names
- Use markers to categorize tests

### 4. Waits
- Always use explicit waits (implemented in BasePage)
- Avoid hard-coded `time.sleep()` when possible
- Use appropriate wait conditions

### 5. Test Data
- Use parametrize for data-driven tests
- Keep test data separate from test logic
- Use fixtures for reusable test setup

## 🔍 Debugging

### Run Tests with Print Statements
```bash
pytest -s  # Shows print statements
```

### Run with Maximum Verbosity
```bash
pytest -vv  # Maximum verbosity
```

### Run with PDB Debugger
```bash
pytest --pdb  # Drops into debugger on failure
```

## 📚 Page Objects Documentation

### BasePage
Common methods available to all page objects:
- `find_element(locator)` - Find single element
- `find_elements(locator)` - Find multiple elements
- `click(locator)` - Click an element
- `send_keys(locator, text)` - Send text to input
- `get_text(locator)` - Get element text
- `is_displayed(locator)` - Check if element is visible
- `select_dropdown_option(locator, value)` - Select dropdown option

### ShopPage
Methods for shop page interactions:
- `perform_search(query)` - Perform search
- `select_category_filter(category)` - Filter by category
- `select_price_filter(price_range)` - Filter by price
- `select_sort_option(sort_value)` - Sort products
- `click_next_page()` - Navigate to next page
- `click_previous_page()` - Navigate to previous page
- `get_product_cards()` - Get all product cards
- `verify_product_display_fields()` - Verify product fields

### HomePage
Methods for home page interactions:
- `perform_search(query)` - Perform search
- `get_product_cards()` - Get product cards
- `verify_product_display_fields()` - Verify product fields

## 🐛 Troubleshooting

### ChromeDriver Issues
If ChromeDriver download fails:
1. Manually download ChromeDriver from https://chromedriver.chromium.org/
2. Add to PATH or specify path in code

### Element Not Found
- Check if locator is correct in `locators/locators.py`
- Verify element exists in HTML
- Increase wait timeout if element loads slowly

### Tests Failing Intermittently
- Add explicit waits
- Increase wait timeouts
- Check for race conditions

## 📊 Test Execution Summary

### Current Test Status
- **Total Test Cases**: 15
- **Implemented**: 15 ✅
- **Test Files**: 3
  - `test_search.py` - 7 tests (TC-1 to TC-6, TC-15)
  - `test_sort_filter.py` - 6 tests (TC-7 to TC-12)
  - `test_pagination.py` - 2 tests (TC-13 to TC-14)

### Test Coverage
- ✅ Search functionality (partial, exact, empty, special chars, long queries)
- ✅ Sorting (price, name)
- ✅ Filtering (category, price range)
- ✅ Combined sorting and filtering
- ✅ Pagination (next, previous)
- ✅ Product display validation

## 📈 Future Enhancements

- [x] Automatic bug report generation ✅
- [x] Screenshot capture on failures ✅
- [x] Live application testing ✅
- [ ] Add API testing
- [ ] Add database validation
- [ ] Add cross-browser testing (Firefox, Edge)
- [ ] Add mobile testing
- [ ] Add performance testing
- [ ] Add CI/CD integration
- [ ] Add Allure reports
- [ ] Add test data management
- [ ] Add test execution in Docker

## 📞 Support

For issues or questions:
1. Check the test logs
2. Review bug reports in `bug_reports/` directory (for failures)
3. Review screenshots in `screenshots/` directory
4. Check HTML reports in `reports/` directory
5. Review locator constants in `locators/locators.py`
6. Check documentation:
   - [BUG_REPORT_GUIDE.md](BUG_REPORT_GUIDE.md) - Bug report documentation
   - [QUICK_REFERENCE.md](QUICK_REFERENCE.md) - Quick command reference
   - [LOCATOR_REVIEW.md](LOCATOR_REVIEW.md) - Complete locator review
   - [FRAMEWORK_SUMMARY.md](FRAMEWORK_SUMMARY.md) - Framework summary

## 📄 License

This test automation framework is part of the StyleZone project.

## 🎯 Quick Links

- **Bug Reports**: See [BUG_REPORT_GUIDE.md](BUG_REPORT_GUIDE.md) for detailed bug report documentation
- **Quick Reference**: See [QUICK_REFERENCE.md](QUICK_REFERENCE.md) for common commands and patterns
- **Locator Review**: See [LOCATOR_REVIEW.md](LOCATOR_REVIEW.md) for complete locator analysis
- **Framework Summary**: See [FRAMEWORK_SUMMARY.md](FRAMEWORK_SUMMARY.md) for implementation details
- **URL Configuration**: See [URL_CONFIGURATION.md](URL_CONFIGURATION.md) for URL setup

## 📝 Key Features Summary

✅ **15 Test Cases** - All test cases implemented and working  
✅ **Page Object Model** - Clean, maintainable architecture  
✅ **Automatic Bug Reports** - Detailed reports on every failure  
✅ **Screenshot Capture** - Automatic screenshots on failures  
✅ **Live Application Testing** - Configured for live URL  
✅ **Multiple Report Formats** - HTML, Markdown, JSON  
✅ **Comprehensive Documentation** - Multiple guides and references  

---

**Last Updated**: 2025-11-23  
**Framework Version**: 1.1.0  
**Application URL**: https://muntasir101.github.io/stylezone

