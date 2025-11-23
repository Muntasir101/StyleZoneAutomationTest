"""
Base page class with common functionality for all page objects.
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


class BasePage:
    """Base class for all page objects"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def find_element(self, locator, timeout=10):
        """Find a single element with explicit wait"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
        except TimeoutException:
            raise NoSuchElementException(f"Element not found: {locator}")
    
    def find_elements(self, locator, timeout=10):
        """Find multiple elements with explicit wait"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
            return self.driver.find_elements(By.CSS_SELECTOR, locator)
        except TimeoutException:
            return []
    
    def click(self, locator, timeout=10):
        """Click an element with explicit wait"""
        element = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))
        element.click()
    
    def send_keys(self, locator, text, timeout=10):
        """Send keys to an element with explicit wait"""
        element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator, timeout=10):
        """Get text from an element"""
        element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
        return element.text
    
    def is_displayed(self, locator, timeout=10):
        """Check if element is displayed"""
        try:
            element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            return element.is_displayed()
        except TimeoutException:
            return False
    
    def is_present(self, locator, timeout=10):
        """Check if element is present in DOM"""
        try:
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
            return True
        except TimeoutException:
            return False
    
    def wait_for_element_invisible(self, locator, timeout=10):
        """Wait for element to be invisible"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, locator)))
            return True
        except TimeoutException:
            return False
    
    def get_current_url(self):
        """Get current page URL"""
        return self.driver.current_url
    
    def navigate_to(self, url):
        """Navigate to a URL"""
        self.driver.get(url)
    
    def get_page_title(self):
        """Get page title"""
        return self.driver.title
    
    def scroll_to_element(self, locator):
        """Scroll to an element"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.5)  # Small delay for scroll animation
    
    def wait_for_page_load(self, timeout=10):
        """Wait for page to load completely"""
        self.wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
    
    def select_dropdown_option(self, locator, value, timeout=10):
        """Select an option from dropdown by value"""
        from selenium.webdriver.support.ui import Select
        element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
        select = Select(element)
        select.select_by_value(value)
    
    def select_dropdown_option_by_text(self, locator, text, timeout=10):
        """Select an option from dropdown by visible text"""
        from selenium.webdriver.support.ui import Select
        element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
        select = Select(element)
        select.select_by_visible_text(text)
    
    def get_dropdown_selected_value(self, locator, timeout=10):
        """Get selected value from dropdown"""
        from selenium.webdriver.support.ui import Select
        element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
        select = Select(element)
        return select.first_selected_option.get_attribute("value")

