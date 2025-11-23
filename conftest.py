"""
Pytest configuration and fixtures for test automation framework.
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
from datetime import datetime
import traceback
from utils.bug_report import BugReportGenerator


@pytest.fixture(scope="session")
def base_url():
    """Base URL for the application"""
    # Get base URL from environment variable or use default live URL
    # Live URL: https://muntasir101.github.io/stylezone
    url = os.getenv("BASE_URL", "https://muntasir101.github.io/stylezone")
    return url


@pytest.fixture(scope="function")
def driver(request):
    """Create and configure WebDriver instance"""
    # Chrome options
    chrome_options = Options()
    
    # Add options based on environment
    if os.getenv("HEADLESS", "false").lower() == "true":
        chrome_options.add_argument("--headless")
    
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--start-maximized")
    
    # Initialize driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Set implicit wait
    driver.implicitly_wait(10)
    
    # Yield driver to test
    yield driver
    
    # Cleanup
    if request.node.rep_call.failed:
        # Take screenshot on failure
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join(screenshot_dir, f"failure_{timestamp}.png")
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved: {screenshot_path}")
        
        # Generate bug report
        try:
            bug_reporter = BugReportGenerator()
            
            # Extract test information
            test_name = request.node.name
            failure_message = str(request.node.rep_call.longrepr) if hasattr(request.node, 'rep_call') else "Test failed"
            
            # Extract test steps from docstring or test name
            test_steps = []
            if hasattr(request.node, 'function') and request.node.function.__doc__:
                docstring = request.node.function.__doc__
                # Try to extract steps from docstring
                lines = docstring.strip().split('\n')
                for line in lines:
                    if line.strip().startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.')):
                        test_steps.append(line.strip())
            
            # Extract expected result from docstring
            expected_result = None
            if hasattr(request.node, 'function') and request.node.function.__doc__:
                docstring = request.node.function.__doc__
                if "Expected:" in docstring:
                    expected_result = docstring.split("Expected:")[-1].strip().split('\n')[0]
            
            # Get environment info
            environment_info = {
                "platform": driver.capabilities.get('platform', 'Unknown'),
                "browser": driver.capabilities.get('browserName', 'Chrome'),
                "browser_version": driver.capabilities.get('browserVersion', 'Unknown'),
                "base_url": os.getenv("BASE_URL", "https://muntasir101.github.io/stylezone"),
                "current_url": driver.current_url
            }
            
            # Generate bug report
            report_id, report_data = bug_reporter.generate_report(
                test_name=test_name,
                failure_message=failure_message,
                screenshot_path=screenshot_path,
                test_steps=test_steps if test_steps else None,
                expected_result=expected_result,
                actual_result="Test failed - see failure message",
                environment_info=environment_info,
                additional_info={
                    "traceback": traceback.format_exc() if hasattr(request.node, 'rep_call') else None,
                    "test_file": request.node.fspath if hasattr(request.node, 'fspath') else None
                }
            )
            
            print(f"\n{'='*60}")
            print("BUG REPORT GENERATED")
            print(f"{'='*60}")
            print(f"Report ID: {report_id}")
            print(f"Test: {test_name}")
            print(f"HTML Report: bug_reports/{report_id}.html")
            print(f"Markdown Report: bug_reports/{report_id}.md")
            print(f"JSON Report: bug_reports/{report_id}.json")
            print(f"{'='*60}\n")
            
        except Exception as e:
            print(f"Warning: Could not generate bug report: {e}")
    
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture test results for screenshots"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope="function")
def home_page(driver, base_url):
    """Fixture to navigate to home page"""
    from pages.home_page import HomePage
    page = HomePage(driver)
    page.navigate_to(f"{base_url}/index.html")
    page.wait_for_page_load()
    return page


@pytest.fixture(scope="function")
def shop_page(driver, base_url):
    """Fixture to navigate to shop page"""
    from pages.shop_page import ShopPage
    page = ShopPage(driver)
    page.navigate_to(f"{base_url}/shop.html")
    page.wait_for_page_load()
    return page

