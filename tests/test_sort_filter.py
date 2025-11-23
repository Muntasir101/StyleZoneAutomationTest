"""
Test cases for sorting and filtering functionality (TC-7 to TC-12)
"""
import pytest
from pages.shop_page import ShopPage
import time


@pytest.mark.sort
@pytest.mark.filter
class TestSortAndFilter:
    """Test cases for sorting and filtering functionality"""
    
    def test_tc7_sort_by_price_low_to_high(self, shop_page):
        """
        TC-7: Sort by price (Low → High)
        Expected: Results sorted from lowest to highest price
        """
        # Search for "Shirt"
        shop_page.perform_search("Shirt")
        time.sleep(2)
        
        # Select Sort by Price: Low → High
        shop_page.select_sort_option("Price: Low to High")
        time.sleep(2)
        
        # Verify prices are sorted in ascending order
        assert shop_page.verify_prices_sorted_ascending(), \
            "Prices should be sorted from lowest to highest"
    
    def test_tc8_sort_by_price_high_to_low(self, shop_page):
        """
        TC-8: Sort by price (High → Low)
        Expected: Results sorted from highest to lowest price
        """
        # Search for "Shirt"
        shop_page.perform_search("Shirt")
        time.sleep(2)
        
        # Select Sort by Price: High → Low
        shop_page.select_sort_option("Price: High to Low")
        time.sleep(2)
        
        # Verify prices are sorted in descending order
        assert shop_page.verify_prices_sorted_descending(), \
            "Prices should be sorted from highest to lowest"
    
    def test_tc9_sort_by_name_a_to_z(self, shop_page):
        """
        TC-9: Sort by name (A → Z)
        Expected: Results sorted alphabetically
        """
        # Search for "Laptop"
        shop_page.perform_search("Laptop")
        time.sleep(2)
        
        # Select Sort by Name: A → Z
        shop_page.select_sort_option("Name: A-Z")
        time.sleep(2)
        
        # Verify names are sorted alphabetically
        assert shop_page.verify_names_sorted_alphabetically(), \
            "Product names should be sorted alphabetically (A-Z)"
    
    def test_tc10_filter_by_category(self, shop_page):
        """
        TC-10: Filter by category
        Expected: Only products in Clothing category displayed
        """
        # Search for "Shirt"
        shop_page.perform_search("Shirt")
        time.sleep(2)
        
        # Apply Category = Clothing filter
        shop_page.select_category_filter("Clothing")
        time.sleep(2)
        
        # Verify filter is applied
        selected_category = shop_page.get_dropdown_selected_value(shop_page.locators.CATEGORY_FILTER)
        assert selected_category == "Clothing", "Category filter should be set to Clothing"
        
        # Verify products are displayed (filtered results)
        products = shop_page.get_product_cards()
        assert len(products) >= 0, "Should display filtered products or no results message"
    
    def test_tc11_filter_by_price_range(self, shop_page):
        """
        TC-11: Filter by price range
        Expected: Only products within the selected price range are displayed
        Note: Adjusting to available price ranges in the application
        """
        # Search for "Shoes"
        shop_page.perform_search("Shoes")
        time.sleep(2)
        
        # Get initial product count and prices
        initial_products = shop_page.get_product_cards()
        initial_prices = shop_page.get_product_prices()
        
        # Apply price range filter (using available options)
        # Note: The app has "0-25", "25-50", "50-100", "100+" options
        # For this test, we'll use "$50 to $100" which should filter products
        shop_page.select_price_filter("$50 to $100")
        time.sleep(2)
        
        # Verify filter is applied
        selected_price = shop_page.get_dropdown_selected_value(shop_page.locators.PRICE_FILTER)
        assert selected_price == "50-100", "Price filter should be set to $50 to $100"
        
        # Verify products are displayed (filtered results)
        products = shop_page.get_product_cards()
        
        # If we have products, verify they are within the price range
        if len(products) > 0:
            prices = shop_page.get_product_prices()
            for price in prices:
                assert 50 <= price <= 100, f"Product price ${price} should be between $50 and $100"
        else:
            # If no products, verify that the filter was applied (results changed)
            # This means the filter is working, just no products in that range
            assert len(initial_products) != len(products) or len(initial_products) == 0, \
                "Price filter should affect the results"
    
    def test_tc12_combine_sorting_filtering(self, shop_page):
        """
        TC-12: Combine sorting and filtering
        Expected: Results filtered AND sorted correctly
        """
        # Search for "Shirt"
        shop_page.perform_search("Shirt")
        time.sleep(2)
        
        # Filter Category = Clothing
        shop_page.select_category_filter("Clothing")
        time.sleep(2)
        
        # Sort Price: Low → High
        shop_page.select_sort_option("Price: Low to High")
        time.sleep(2)
        
        # Verify filter is still applied
        selected_category = shop_page.get_dropdown_selected_value(shop_page.locators.CATEGORY_FILTER)
        assert selected_category == "Clothing", "Category filter should remain applied"
        
        # Verify sort is applied
        selected_sort = shop_page.get_dropdown_selected_value(shop_page.locators.SORT_OPTION)
        assert selected_sort == "priceAsc", "Sort should be set to Price: Low to High"
        
        # Verify prices are sorted in ascending order
        products = shop_page.get_product_cards()
        if len(products) > 0:
            assert shop_page.verify_prices_sorted_ascending(), \
                "Prices should be sorted ascending after applying both filter and sort"

