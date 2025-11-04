from behave import given, then, when

from utils.helpers import URLS, fill_cart_script, login_cookie


@given("I'm authenticated and in pre-filled shopping cart page")
def step_authenticate_and_prefill_cart(context):
    context.page.context.add_cookies([login_cookie()])
    context.page.context.add_init_script(script=fill_cart_script())
    context.page_object.navigate_to_page(url=URLS["CART_PAGE"], title="Your Cart")


@when("I click the button 'Continue shopping'")
def step_click_continue_shopping(context):
    context.page_object.return_to_shop_page()


@when("I click the button 'Checkout'")
def step_click_checkout(context):
    context.page_object.proceed_to_checkout_page()


@when("I click 'Remove' on a cart item")
def step_click_remove_item(context):
    context.page_object.remove_first_item_from_cart()


@then("I should be redirected back to the shop")
def step_redirect_back_to_shop(context):
    context.page_object.current_page_should_be(
        expected_url=URLS["INVENTORY_PAGE"], title="Products"
    )


@then("I should be redirected to first step of the checkout")
def step_redirect_to_checkout(context):
    context.page_object.current_page_should_be(
        expected_url=URLS["CHECKOUT_PAGE1"], title="Checkout: Your Information"
    )


@then("The item should be removed and the amount of items in cart reduced")
def step_item_is_removed_and_count_reduced(context):
    assert context.page_object.get_cart_item_count() == 5
