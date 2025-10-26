from behave import given, when, then
from utils.helpers import login_cookie, fill_cart_script


@given("I am on the inventory page")
def step_open_inventor_page(context):
    context.page.context.add_cookies([login_cookie()])
    context.page_object.navigate_to_inventory_page()

@when("I add two item to the cart")
def step_add_two_items_to_cart(context):
    context.page_object.add_items_to_cart(amount_of_items=2)

@then("I should see two items indicated by tye shopping cart badge")
def step_cart_should_have_two_items(context):
    assert context.page_object.cart_item_count() == 2