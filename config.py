"""
Configuration file for test automation framework
"""
import os

# Application URLs
BASE_URL = os.getenv("BASE_URL", "https://muntasir101.github.io/stylezone")
HOME_PAGE_URL = f"{BASE_URL}/index.html"
SHOP_PAGE_URL = f"{BASE_URL}/shop.html"
PRODUCT_PAGE_URL = f"{BASE_URL}/product.html"
CHECKOUT_PAGE_URL = f"{BASE_URL}/checkout.html"

# Browser Configuration
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
BROWSER = os.getenv("BROWSER", "chrome")

# Wait Timeouts
IMPLICIT_WAIT = 10
EXPLICIT_WAIT = 10
PAGE_LOAD_TIMEOUT = 30

# Test Configuration
SCREENSHOT_ON_FAILURE = True
SCREENSHOT_DIR = "screenshots"
REPORT_DIR = "reports"

# Application-specific settings
ITEMS_PER_PAGE = 12
MAX_SEARCH_QUERY_LENGTH = 100

