from behave import given, when, then
from utils.helpers import login_cookie


@given("I am on the inventory page")
def step_open_inventory_page(context):
    context.page.context.add_cookies([login_cookie()])
    context.page_object.navigate_to_inventory_page()

@when("I add two items to the cart")
def step_add_two_items_to_cart(context):
    context.page_object.add_items_to_cart(amount_of_items=2)

@when("I remove one of the items from cart")
def step_remove_item_from_cart(context):
    context.page_object.remove_items_from_cart(amount_of_items=1)

@when("I sort the products by 'Name (Z to A)'")
def step_sort_by_name_reverse(context):
    context.page_object.use_inventory_filter("Name (Z to A)")

@when("I sort the products by 'Name (A to Z)'")
def step_sort_by_name(context):
    context.page_object.use_inventory_filter("Name (A to Z)")

@when("I sort the products by 'Price (low to high)'")
def step_sort_by_price(context):
    context.page_object.use_inventory_filter("Price (low to high)")

@when("I sort the products by 'Price (high to low)'")
def step_sort_by_price_reverse(context):
    context.page_object.use_inventory_filter("Price (high to low)")

@then("I should see all products with a title, picture, description and a price")
def step_verify_product_contents(context):
    context.page_object.verify_inventory_item_contents()

@then("I should see two items indicated by the shopping cart badge")
def step_cart_should_have_two_items(context):
    assert context.page_object.cart_item_count() == 2

@then("I should see the amount of cart items reduced to one")
def step_cart_items_are_reduced(context):
    assert context.page_object.cart_item_count() == 1

@then("The products should be reverse sorted by names")
def step_products_sorted_by_name(context):
    context.page_object.verify_items_are_ordered_by_name(reverse=True)

@then("The products should be sorted by names")
def step_products_sorted_by_name(context):
    context.page_object.verify_items_are_ordered_by_name(reverse=False)

@then("The products should be sorted by prices")
def step_products_sorted_by_price(context):
    context.page_object.verify_items_are_ordered_by_price(reverse=False)

@then("The products should be reverse sorted by prices")
def step_products_sorted_by_price(context):
    context.page_object.verify_items_are_ordered_by_price(reverse=True)
