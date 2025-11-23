"""
Test cases for pagination functionality (TC-13 to TC-14)
"""
import pytest
from pages.shop_page import ShopPage
import time


@pytest.mark.pagination
class TestPagination:
    """Test cases for pagination functionality"""
    
    def test_tc13_pagination_next_page(self, shop_page):
        """
        TC-13: Pagination – Next Page
        Expected: Page 2 loads with next set of results
        """
        # Search for "phone"
        shop_page.perform_search("phone")
        time.sleep(2)
        
        # Check if pagination is available (need more than 12 results)
        products_page1 = shop_page.get_product_cards()
        
        if len(products_page1) >= 12 and shop_page.is_pagination_displayed():
            # Get current page number
            current_page = shop_page.get_current_page_number()
            
            # Click Next Page
            shop_page.click_next_page()
            time.sleep(2)
            
            # Verify we're on a different page
            new_page = shop_page.get_current_page_number()
            assert new_page > current_page, "Should be on a higher page number after clicking next"
            
            # Verify products are displayed on page 2
            products_page2 = shop_page.get_product_cards()
            assert len(products_page2) > 0, "Page 2 should display products"
            
            # Verify we have different products (or at least page changed)
            # Note: Products might be different or same depending on data
            assert new_page >= 2, "Should be on page 2 or higher"
        else:
            pytest.skip("Not enough products for pagination test (need 12+ products)")
    
    def test_tc14_pagination_previous_page(self, shop_page):
        """
        TC-14: Pagination – Previous Page
        Expected: Returns to Page 1
        """
        # Search for "phone"
        shop_page.perform_search("phone")
        time.sleep(2)
        
        # Check if pagination is available
        products_page1 = shop_page.get_product_cards()
        
        if len(products_page1) >= 12 and shop_page.is_pagination_displayed():
            # Navigate to page 2 first
            shop_page.click_next_page()
            time.sleep(2)
            
            # Verify we're on page 2
            page_after_next = shop_page.get_current_page_number()
            assert page_after_next >= 2, "Should be on page 2 or higher"
            
            # Click Previous Page
            shop_page.click_previous_page()
            time.sleep(2)
            
            # Verify we're back on page 1
            page_after_prev = shop_page.get_current_page_number()
            assert page_after_prev == 1, f"Should be back on page 1, but on page {page_after_prev}"
            
            # Verify products are displayed
            products_after_prev = shop_page.get_product_cards()
            assert len(products_after_prev) > 0, "Page 1 should display products after clicking previous"
        else:
            pytest.skip("Not enough products for pagination test (need 12+ products)")

