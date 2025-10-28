from behave import given, when, then
from utils.helpers import login_cookie


@given("I'm authenticated and on the inventory page")
def step_authenticate(context):
    context.page.context.add_cookies([login_cookie()])
    context.page.goto("https://www.saucedemo.com/inventory.html")

@when("I open the side navigation menu")
def step_open_nav_menu(context):
    context.page_object.open_side_menu()

@when("I navigate to the shopping cart page")
def navigate_to_cart(context):
    context.page.goto("https://www.saucedemo.com/cart.html")

@when("I choose the option 'All Items'")
def step_choose_all_items(context):
    context.page_object.menu_all_items_button.click()

@when("I choose the option 'About'")
def step_choose_about(context):
    context.page_object.menu_about_button.click()

@when("I choose the option 'Logout'")
def step_choose_logout(context):
    context.page_object.menu_logout_button.click()

@then("I can close the menu")
def step_close_menu(context):
    context.page_object.close_side_menu()

@then("I should be redirected to the inventory page")
def step_redirect_to_inventory(context):
    context.page_object.verify_navigation("https://www.saucedemo.com/inventory.html")

@then("I should be redirected to the SauceLabs 'About' page")
def step_redirect_to_about_page(context):
    context.page_object.verify_navigation("https://saucelabs.com/")

@then("I should be redirected to the login page")
def step_redirect_to_login_page(context):
    context.page_object.verify_navigation("https://www.saucedemo.com/")
