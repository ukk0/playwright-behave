from behave import given, then, when

from utils.helpers import URLS, login_cookie


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


@when("I click on the 'X' button in footer")
def step_navigate_to_x(context):
    """
    Syntax sugar, we need to combine the clicking and expectation
    in the method used for related 'Then'.
    """


@when("I click on the 'Facebook' button in footer")
def step_navigate_to_fb(context):
    """
    Syntax sugar, we need to combine the clicking and expectation
    in the method used for related 'Then'.
    """


@when("I click on the 'LinkedIn' button in footer")
def step_navigate_to_li(context):
    """
    Syntax sugar, we need to combine the clicking and expectation
    in the method used for related 'Then'.
    """


@then("I can close the menu")
def step_close_menu(context):
    context.page_object.close_side_menu()


@then("I should be redirected to the inventory page")
def step_redirect_to_inventory(context):
    context.page_object.current_page_should_be(expected_url=URLS["INVENTORY_PAGE"])


@then("I should be redirected to the SauceLabs 'About' page")
def step_redirect_to_about_page(context):
    context.page_object.current_page_should_be(expected_url=URLS["ABOUT_PAGE"])


@then("I should be redirected to the login page")
def step_redirect_to_login_page(context):
    context.page_object.current_page_should_be(expected_url=URLS["LOGIN_PAGE"])


@then("I should be redirected to SauceLabs X page")
def step_redirect_to_x(context):
    context.page_object.page_in_new_tab_should_have_url(
        locator=context.page_object.link_button_x, expected_url=URLS["SOC_X_PAGE"]
    )


@then("I should be redirected to SauceLabs Facebook page")
def step_redirect_to_fb(context):
    context.page_object.page_in_new_tab_should_have_url(
        locator=context.page_object.link_button_fb, expected_url=URLS["SOC_FB_PAGE"]
    )


@then("I should be redirected to SauceLabs LinkedIn page")
def step_redirect_to_li(context):
    context.page_object.page_in_new_tab_should_have_url(
        locator=context.page_object.link_button_li, expected_url=URLS["SOC_LI_PAGE"]
    )
