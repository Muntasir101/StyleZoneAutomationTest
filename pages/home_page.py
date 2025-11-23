"""
Home page object for index.html
"""
from pages.base_page import BasePage
from locators.locators import HomePageLocators
import time


class HomePage(BasePage):
    """Home page object"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = HomePageLocators
    
    def enter_search_query(self, query):
        """Enter search query in the search input"""
        self.send_keys(self.locators.SEARCH_INPUT, query)
        time.sleep(0.5)  # Wait for debounce
    
    def click_search_button(self):
        """Click the search button"""
        self.click(self.locators.SEARCH_BUTTON)
        time.sleep(1)  # Wait for search results
    
    def perform_search(self, query):
        """Perform a complete search action"""
        self.enter_search_query(query)
        self.click_search_button()
        time.sleep(2)  # Wait for results to load
    
    def get_search_results_count(self):
        """Get the search results count text"""
        if self.is_present(self.locators.SEARCH_RESULTS_COUNT):
            return self.get_text(self.locators.SEARCH_RESULTS_COUNT)
        return ""
    
    def is_search_results_displayed(self):
        """Check if search results section is displayed"""
        return self.is_displayed(self.locators.SEARCH_RESULTS_SECTION)
    
    def get_product_cards(self):
        """Get all product cards from search results"""
        if self.is_present(self.locators.SEARCH_RESULTS_GRID):
            return self.find_elements(f"{self.locators.SEARCH_RESULTS_GRID} .product-card")
        return []
    
    def get_product_names(self):
        """Get all product names from search results"""
        products = self.get_product_cards()
        names = []
        for product in products:
            try:
                name_element = product.find_element(By.CSS_SELECTOR, ".product-name")
                names.append(name_element.text)
            except:
                continue
        return names
    
    def get_product_prices(self):
        """Get all product prices from search results"""
        products = self.get_product_cards()
        prices = []
        for product in products:
            try:
                price_element = product.find_element(By.CSS_SELECTOR, ".product-price")
                price_text = price_element.text.replace("$", "").strip()
                prices.append(float(price_text))
            except:
                continue
        return prices
    
    def verify_product_display_fields(self):
        """Verify that each product displays name, price, and image"""
        products = self.get_product_cards()
        if not products:
            return False
        
        for product in products:
            try:
                # Check for name
                name = product.find_element(By.CSS_SELECTOR, ".product-name")
                if not name.text:
                    return False
                
                # Check for price
                price = product.find_element(By.CSS_SELECTOR, ".product-price")
                if not price.text:
                    return False
                
                # Check for image
                image = product.find_element(By.CSS_SELECTOR, ".product-image img")
                if not image.get_attribute("src"):
                    return False
            except:
                return False
        
        return True
    
    def close_search_results(self):
        """Close the search results section"""
        if self.is_present(self.locators.CLOSE_SEARCH_RESULTS):
            self.click(self.locators.CLOSE_SEARCH_RESULTS)
            time.sleep(0.5)
    
    def get_cart_count(self):
        """Get the current cart count"""
        if self.is_present(self.locators.CART_COUNT):
            try:
                return int(self.get_text(self.locators.CART_COUNT))
            except:
                return 0
        return 0

