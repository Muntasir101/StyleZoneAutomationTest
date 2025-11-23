"""
Locator constants for StyleZone e-commerce application.
All locators are organized by page and functionality.
"""


class HomePageLocators:
    """Locators for the home page (index.html)"""
    # Search
    SEARCH_INPUT = "#homeSearchInput"
    SEARCH_BUTTON = ".search-button"
    SEARCH_RESULTS_SECTION = "#searchResultsSection"
    SEARCH_RESULTS_GRID = "#searchResultsGrid"
    SEARCH_RESULTS_COUNT = "#searchResultsCount"
    CLOSE_SEARCH_RESULTS = ".close-search-results"
    
    # Navigation
    CART_ICON = "#cartIcon"
    CART_COUNT = ".cart-count"
    LOGO = ".logo"
    
    # Product sections
    DEALS_GRID = "#dealsGrid"
    BESTSELLERS_GRID = "#bestsellersGrid"
    FAVORITES_GRID = "#favoritesGrid"
    
    # Newsletter
    NEWSLETTER_FORM = "#newsletterForm"
    NEWSLETTER_EMAIL_INPUT = "input[type='email']"


class ShopPageLocators:
    """Locators for the shop page (shop.html)"""
    # Search
    SEARCH_INPUT = ".search-input"
    SEARCH_BUTTON = ".search-button"
    
    # Filters
    CATEGORY_FILTER = "#categoryFilter"
    PRICE_FILTER = "#priceFilter"
    RATING_FILTER = "#ratingFilter"
    SHIPPING_FILTER = "#shippingFilter"
    RESET_FILTERS_BUTTON = "#resetFilters"
    
    # Sort
    SORT_OPTION = "#sortOption"
    
    # Results
    PRODUCT_RESULTS = "#productResults"
    RESULTS_COUNT = ".results-count"
    
    # Pagination
    PAGINATION = "#pagination"
    PAGINATION_BUTTON = ".pagination-button"
    PAGINATION_PREV = "button[data-page='prev']"
    PAGINATION_NEXT = "button[data-page='next']"
    
    # Product cards
    PRODUCT_CARD = ".product-card"
    PRODUCT_NAME = ".product-name"
    PRODUCT_PRICE = ".product-price"
    PRODUCT_IMAGE = ".product-image img"
    ADD_TO_CART = ".add-to-cart"
    
    # Cart
    CART_ICON = "#cartIcon"
    CART_MODAL = "#cartModal"
    CART_COUNT = ".cart-count"
    CLOSE_CART = ".close-cart"
    
    # Empty state
    NO_RESULTS_MESSAGE = "p[style*='No products match']"


class ProductDetailPageLocators:
    """Locators for the product detail page (product.html)"""
    PRODUCT_DETAILS = "#productDetails"
    PRODUCT_NAME = "#productDetails h2"
    PRODUCT_PRICE = ".product-price"
    PRODUCT_IMAGE = ".product-image img"
    ADD_TO_CART = ".add-to-cart"
    CART_COUNT = ".cart-count"


class CheckoutPageLocators:
    """Locators for the checkout page (checkout.html)"""
    CHECKOUT_FORM = "#checkoutForm"
    FULL_NAME = "#fullName"
    ADDRESS = "#address"
    CITY = "#city"
    POSTAL_CODE = "#postalCode"
    COUNTRY = "#country"
    PLACE_ORDER_BUTTON = "#placeOrderBtn"
    EMPTY_CART_MESSAGE = "#emptyCartMessage"


class CommonLocators:
    """Locators common across all pages"""
    CART_ICON = "#cartIcon"
    CART_COUNT = ".cart-count"
    NAVBAR = ".navbar"
    FOOTER = ".footer"
    LOADING = ".loading"

