# Quick Reference Guide - Test Automation Framework

## 🚀 Quick Commands

### Setup (First Time Only)
```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Linux/Mac)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Run Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_search.py
pytest tests/test_sort_filter.py
pytest tests/test_pagination.py

# Run specific test
pytest tests/test_search.py::TestSearchFunctionality::test_tc1_successful_search_partial_case_insensitive

# Run by marker
pytest -m search
pytest -m sort
pytest -m filter
pytest -m pagination
pytest -m smoke

# Run with HTML report
pytest --html=reports/report.html --self-contained-html

# Run in parallel
pytest -n auto

# Run with verbose output
pytest -v

# Run with maximum verbosity
pytest -vv
```

## 📋 Test Cases Quick Reference

| TC ID | Test Name | File | Marker |
|-------|-----------|------|--------|
| TC-1 | Successful search (partial, case-insensitive) | test_search.py | search, smoke |
| TC-2 | Exact match search | test_search.py | search |
| TC-3 | No results found | test_search.py | search |
| TC-4 | Empty search returns all products | test_search.py | search |
| TC-5 | Query with special characters | test_search.py | search |
| TC-6 | Long query truncation | test_search.py | search |
| TC-7 | Sort by price (Low → High) | test_sort_filter.py | sort |
| TC-8 | Sort by price (High → Low) | test_sort_filter.py | sort |
| TC-9 | Sort by name (A → Z) | test_sort_filter.py | sort |
| TC-10 | Filter by category | test_sort_filter.py | filter |
| TC-11 | Filter by price range | test_sort_filter.py | filter |
| TC-12 | Combine sorting and filtering | test_sort_filter.py | sort, filter |
| TC-13 | Pagination – Next Page | test_pagination.py | pagination |
| TC-14 | Pagination – Previous Page | test_pagination.py | pagination |
| TC-15 | Verify product display fields | test_search.py | search |

## 🔍 Common Locators

### Shop Page
```python
# Search
SEARCH_INPUT = ".search-input"
SEARCH_BUTTON = ".search-button"

# Filters
CATEGORY_FILTER = "#categoryFilter"
PRICE_FILTER = "#priceFilter"
RATING_FILTER = "#ratingFilter"
SHIPPING_FILTER = "#shippingFilter"

# Sort
SORT_OPTION = "#sortOption"

# Results
PRODUCT_RESULTS = "#productResults"
PRODUCT_CARD = ".product-card"
PRODUCT_NAME = ".product-name"
PRODUCT_PRICE = ".product-price"
PRODUCT_IMAGE = ".product-image img"

# Pagination
PAGINATION = "#pagination"
PAGINATION_NEXT = "button[data-page='next']"
PAGINATION_PREV = "button[data-page='prev']"
```

### Home Page
```python
SEARCH_INPUT = "#homeSearchInput"
SEARCH_BUTTON = ".search-button"
SEARCH_RESULTS_GRID = "#searchResultsGrid"
```

## 🛠️ Common Page Object Methods

### ShopPage
```python
# Search
shop_page.perform_search("laptop")
shop_page.enter_search_query("laptop")
shop_page.click_search_button()

# Filters
shop_page.select_category_filter("Clothing")
shop_page.select_price_filter("$100 & Above")
shop_page.select_rating_filter("4")
shop_page.reset_filters()

# Sort
shop_page.select_sort_option("Price: Low to High")
shop_page.select_sort_option("Price: High to Low")
shop_page.select_sort_option("Name: A-Z")

# Products
products = shop_page.get_product_cards()
names = shop_page.get_product_names()
prices = shop_page.get_product_prices()
shop_page.verify_product_display_fields()

# Pagination
shop_page.click_next_page()
shop_page.click_previous_page()
shop_page.is_pagination_displayed()
```

### HomePage
```python
home_page.perform_search("laptop")
home_page.get_product_cards()
home_page.verify_product_display_fields()
```

## 📁 File Locations

| Item | Location |
|------|----------|
| Locators | `locators/locators.py` |
| Page Objects | `pages/*.py` |
| Test Cases | `tests/test_*.py` |
| Configuration | `conftest.py`, `pytest.ini` |
| Reports | `reports/report.html` |
| Screenshots | `screenshots/` |

## 🎯 Common Patterns

### Wait for Element
```python
element = page.find_element(locator)
```

### Click Element
```python
page.click(locator)
```

### Enter Text
```python
page.send_keys(locator, "text")
```

### Get Text
```python
text = page.get_text(locator)
```

### Check if Displayed
```python
is_visible = page.is_displayed(locator)
```

### Select Dropdown
```python
page.select_dropdown_option(locator, "value")
page.select_dropdown_option_by_text(locator, "Text")
```

## 🐛 Debugging

```bash
# Run with print statements
pytest -s

# Run with debugger
pytest --pdb

# Run with traceback
pytest --tb=short
pytest --tb=long
```

## 📊 Reports

```bash
# Generate HTML report
pytest --html=reports/report.html --self-contained-html

# View report
# Open reports/report.html in browser
```

## ⚙️ Environment Variables

```bash
# Set base URL (default: https://muntasir101.github.io/stylezone)
export BASE_URL="https://muntasir101.github.io/stylezone"

# Run headless
export HEADLESS="true"
```

## 🔄 Common Workflows

### Run All Search Tests
```bash
pytest -m search -v
```

### Run All Sort Tests
```bash
pytest -m sort -v
```

### Run All Tests with Report
```bash
pytest --html=reports/report.html --self-contained-html -v
```

### Run Specific Test Case
```bash
pytest tests/test_search.py::TestSearchFunctionality::test_tc1_successful_search_partial_case_insensitive -v
```

---

**Quick Tip**: Use `pytest -v` for verbose output to see which tests are running.

