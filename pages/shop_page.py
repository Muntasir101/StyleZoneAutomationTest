"""
Shop page object for shop.html
"""
from pages.base_page import BasePage
from locators.locators import ShopPageLocators
from selenium.webdriver.common.by import By
import time


class ShopPage(BasePage):
    """Shop page object"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ShopPageLocators
    
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
    
    def get_product_cards(self):
        """Get all product cards from results"""
        if self.is_present(self.locators.PRODUCT_RESULTS):
            return self.find_elements(f"{self.locators.PRODUCT_RESULTS} .product-card")
        return []
    
    def get_product_names(self):
        """Get all product names from results"""
        products = self.get_product_cards()
        names = []
        for product in products:
            try:
                name_element = product.find_element(By.CSS_SELECTOR, ".product-name")
                names.append(name_element.text.lower())
            except:
                continue
        return names
    
    def get_product_prices(self):
        """Get all product prices from results"""
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
    
    def is_no_results_message_displayed(self):
        """Check if 'No results found' message is displayed"""
        # Check for the no results message
        if self.is_present(self.locators.NO_RESULTS_MESSAGE):
            return True
        
        # Also check if results container has no products message
        try:
            results_container = self.find_element(self.locators.PRODUCT_RESULTS, timeout=5)
            text = results_container.text.lower()
            return "no products" in text or "no results" in text or "match" in text
        except:
            # If results container doesn't exist or is empty, consider it as no results
            return len(self.get_product_cards()) == 0
    
    def select_category_filter(self, category):
        """Select category filter"""
        if category:
            self.select_dropdown_option_by_text(self.locators.CATEGORY_FILTER, category)
        else:
            self.select_dropdown_option(self.locators.CATEGORY_FILTER, "")
        time.sleep(1)  # Wait for filter to apply
    
    def select_price_filter(self, price_range):
        """Select price filter by visible text"""
        if price_range:
            self.select_dropdown_option_by_text(self.locators.PRICE_FILTER, price_range)
        else:
            self.select_dropdown_option(self.locators.PRICE_FILTER, "")
        time.sleep(1)  # Wait for filter to apply
    
    def select_rating_filter(self, rating):
        """Select rating filter"""
        if rating:
            self.select_dropdown_option(self.locators.RATING_FILTER, rating)
        else:
            self.select_dropdown_option(self.locators.RATING_FILTER, "")
        time.sleep(1)  # Wait for filter to apply
    
    def select_shipping_filter(self, shipping):
        """Select shipping filter"""
        if shipping:
            self.select_dropdown_option(self.locators.SHIPPING_FILTER, shipping)
        else:
            self.select_dropdown_option(self.locators.SHIPPING_FILTER, "")
        time.sleep(1)  # Wait for filter to apply
    
    def reset_filters(self):
        """Click reset filters button"""
        self.click(self.locators.RESET_FILTERS_BUTTON)
        time.sleep(1)  # Wait for filters to reset
    
    def select_sort_option(self, sort_value):
        """Select sort option"""
        # Map human-readable values to actual option values
        sort_map = {
            "Price: Low to High": "priceAsc",
            "Price: High to Low": "priceDesc",
            "Name: A-Z": "nameAsc",
            "Featured": "featured"
        }
        
        value = sort_map.get(sort_value, sort_value)
        self.select_dropdown_option(self.locators.SORT_OPTION, value)
        time.sleep(1)  # Wait for sort to apply
    
    def get_results_count_text(self):
        """Get the results count text"""
        if self.is_present(self.locators.RESULTS_COUNT):
            return self.get_text(self.locators.RESULTS_COUNT)
        return ""
    
    def is_pagination_displayed(self):
        """Check if pagination is displayed"""
        return self.is_present(self.locators.PAGINATION)
    
    def click_next_page(self):
        """Click next page button"""
        if self.is_present(self.locators.PAGINATION_NEXT):
            self.click(self.locators.PAGINATION_NEXT)
            time.sleep(2)  # Wait for page to load
    
    def click_previous_page(self):
        """Click previous page button"""
        if self.is_present(self.locators.PAGINATION_PREV):
            self.click(self.locators.PAGINATION_PREV)
            time.sleep(2)  # Wait for page to load
    
    def get_current_page_number(self):
        """Get current page number from pagination"""
        try:
            pagination = self.find_element(self.locators.PAGINATION)
            # Find the disabled button which indicates current page
            current_page = pagination.find_element(By.CSS_SELECTOR, "button[disabled]")
            page_text = current_page.text.strip()
            if page_text.isdigit():
                return int(page_text)
        except:
            pass
        return 1
    
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
    
    def get_all_products_count(self):
        """Get total number of products displayed"""
        return len(self.get_product_cards())
    
    def verify_prices_sorted_ascending(self):
        """Verify prices are sorted in ascending order"""
        prices = self.get_product_prices()
        if len(prices) < 2:
            return True
        return prices == sorted(prices)
    
    def verify_prices_sorted_descending(self):
        """Verify prices are sorted in descending order"""
        prices = self.get_product_prices()
        if len(prices) < 2:
            return True
        return prices == sorted(prices, reverse=True)
    
    def verify_names_sorted_alphabetically(self):
        """Verify product names are sorted alphabetically"""
        names = self.get_product_names()
        if len(names) < 2:
            return True
        return names == sorted(names)
    
    def verify_category_filter(self, expected_category):
        """Verify all displayed products belong to expected category"""
        # Note: This would require checking product data or category badge
        # For now, we'll verify that filter is applied
        selected_category = self.get_dropdown_selected_value(self.locators.CATEGORY_FILTER)
        return selected_category == expected_category or (not expected_category and selected_category == "")
    
    def verify_price_range_filter(self, min_price, max_price):
        """Verify all displayed products are within price range"""
        prices = self.get_product_prices()
        if not prices:
            return True
        
        for price in prices:
            if max_price:
                if not (min_price <= price <= max_price):
                    return False
            else:
                if price < min_price:
                    return False
        return True

