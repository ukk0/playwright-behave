from behave import given, when, then
from utils.helpers import login_cookie, URLS


@given("I'm authenticated and on the inventory page")
def step_authenticate(context):
    context.page.context.add_cookies([login_cookie()])
    context.page_object.navigate_to_page(URLS["INVENTORY_PAGE"])

@when("I open the side navigation menu")
def step_open_nav_menu(context):
    context.page_object.open_side_menu()

@when("I navigate to the shopping cart page")
def step_navigate_to_cart(context):
    context.page_object.navigate_to_page(URLS["CART_PAGE"], title="Your Cart")

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
    context.page_object.current_page_should_be(
        expected_url=URLS["INVENTORY_PAGE"]
    )

@then("I should be redirected to the SauceLabs 'About' page")
def step_redirect_to_about_page(context):
    context.page_object.current_page_should_be(
        expected_url=URLS["ABOUT_PAGE"]
    )

@then("I should be redirected to the login page")
def step_redirect_to_login_page(context):
    context.page_object.current_page_should_be(
        expected_url=URLS["LOGIN_PAGE"]
    )
