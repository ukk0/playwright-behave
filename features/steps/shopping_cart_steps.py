from behave import given, when, then
from utils.helpers import login_cookie, fill_cart_script, urls


@given("I'm authenticated and in pre-filled shopping cart page")
def step_authenticate_and_prefill_cart(context):
    pass

@when("I click the button 'Continue shopping'")
def step_click_continue_shopping(context):
    pass

@when("I click the button 'Checkout'")
def step_click_checkout(context):
    pass

@when("I click 'Remove' on a cart item")
def step_click_remove_item(context):
    pass

@then("I should be redirected back to the shop")
def step_redirect_back_to_shop(context):
    pass

@then("I should be redirected to first step of the checkout")
def step_redirect_to_checkout(context):
    pass

@then("The item should be removed and the amount of items in cart is reduced")
def step_item_is_removed_and_count_reduced(context):
    pass
