"""
Demo test to demonstrate bug report generation
This test intentionally fails to show bug report functionality
"""
import pytest


@pytest.mark.search
class TestBugReportDemo:
    """Demo test class for bug report generation"""
    
    def test_demo_failure_for_bug_report(self, shop_page):
        """
        Demo test that fails to demonstrate bug report generation
        
        Steps:
        1. Navigate to shop page
        2. Search for "NonExistentProduct12345"
        3. Verify products are displayed
        
        Expected: Products should be displayed
        """
        import time
        
        # This search will likely return no results
        shop_page.perform_search("NonExistentProduct12345")
        time.sleep(2)
        
        # This assertion will fail intentionally to demonstrate bug report
        products = shop_page.get_product_cards()
        assert len(products) > 0, "This test intentionally fails to demonstrate bug report generation"
        
        # Verify product names
        product_names = shop_page.get_product_names()
        assert len(product_names) > 0, "Should have product names"

