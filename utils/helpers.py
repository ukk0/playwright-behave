urls = {
    "ABOUT_PAGE": "https://saucelabs.com/",
    "LOGIN_PAGE": "https://www.saucedemo.com/",
    "INVENTORY_PAGE": "https://www.saucedemo.com/inventory.html",
    "CART_PAGE": "https://www.saucedemo.com/cart.html",
}

def login_cookie():
    return {
        "name": "session-username",
        "value": "standard_user",
        "domain": "www.saucedemo.com",
        "path": "/",
    }

def fill_cart_script():
    return "localStorage.setItem('cart-contents', '[0, 1, 2, 3, 4, 5]')"
