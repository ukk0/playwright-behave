from behave import given, when, then
from utils.helpers import login_cookie


@given("I am on the inventory page")
def step_open_inventor_page(context):
    context.page.context.add_cookies([login_cookie()])
    context.page_object.navigate_to_inventory_page()

@then("I should see all products with a title, picture, description and a price")
def step_verify_product_contents(context):
    context.page_object.verify_inventory_item_contents()

@when("I add two items to the cart")
def step_add_two_items_to_cart(context):
    context.page_object.add_items_to_cart(amount_of_items=2)

@then("I should see two items indicated by the shopping cart badge")
def step_cart_should_have_two_items(context):
    assert context.page_object.cart_item_count() == 2

@when("I remove one of the items from cart")
def step_remove_item_from_cart(context):
    context.page_object.remove_items_from_cart(amount_of_items=1)

@then("I should see the amount of cart items reduced to one")
def step_cart_items_are_reduced(context):
    assert context.page_object.cart_item_count() == 1
