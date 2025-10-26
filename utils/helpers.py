def login_cookie():
    cookie = {
        "name": "session-username",
        "value": "standard_user",
        "domain": "www.saucedemo.com",
        "path": "/",
    }
    return cookie

def fill_cart_script():
    init_script = "localStorage.setItem('cart-contents', '[0, 1, 2, 3, 4, 5]')"
    return init_script