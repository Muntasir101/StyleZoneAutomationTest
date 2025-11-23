# URL Configuration Update

## ✅ Framework Updated for Live Application

The test automation framework has been configured to work with the live application:

**Live URL**: [https://muntasir101.github.io/stylezone/index.html](https://muntasir101.github.io/stylezone/index.html)

## 🔧 Configuration Changes

### 1. **conftest.py Updated**
- Default `BASE_URL` changed from local file path to live URL
- Now uses: `https://muntasir101.github.io/stylezone`

### 2. **config.py Created**
- Centralized configuration file
- Contains all URLs and settings
- Easy to update for different environments

### 3. **Documentation Updated**
- README_TEST_FRAMEWORK.md
- QUICK_REFERENCE.md
- Both now reference the live URL

## 🌐 Application URLs

The framework now uses these URLs:

| Page | URL |
|------|-----|
| Home Page | `https://muntasir101.github.io/stylezone/index.html` |
| Shop Page | `https://muntasir101.github.io/stylezone/shop.html` |
| Product Page | `https://muntasir101.github.io/stylezone/product.html` |
| Checkout Page | `https://muntasir101.github.io/stylezone/checkout.html` |

## 🚀 Running Tests

Tests will now automatically use the live URL:

```bash
# Run all tests (uses live URL by default)
pytest

# Or explicitly set URL via environment variable
export BASE_URL="https://muntasir101.github.io/stylezone"
pytest
```

## 🔄 Switching Between Environments

### Use Live URL (Default)
```bash
pytest  # Uses live URL automatically
```

### Use Local Files
```bash
# Set environment variable for local testing
export BASE_URL="file:///path/to/local/project"
pytest
```

### Use Different Environment
```bash
# Set custom URL
export BASE_URL="https://your-custom-url.com"
pytest
```

## ✅ Verification

To verify the framework is using the correct URL:

1. Run a test with verbose output:
   ```bash
   pytest tests/test_search.py::TestSearchFunctionality::test_tc1_successful_search_partial_case_insensitive -v -s
   ```

2. Check the browser opens the correct URL
3. Verify tests can interact with the live application

## 📝 Notes

- The framework is now ready to test the live application
- All locators should work with the live site
- Tests will run against the actual deployed application
- Screenshots and reports will be generated as before

---

**Updated**: 2025-01-27  
**Status**: ✅ Ready to test live application

