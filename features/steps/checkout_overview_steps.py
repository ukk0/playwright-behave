from behave import given, when, then
from utils.helpers import login_cookie, fill_cart_script, URLS

@given("I'm authenticated and on the final checkout overview")
def step_final_checkout(context):
    context.page.context.add_cookies([login_cookie()])
    context.page.context.add_init_script(script=fill_cart_script())
    context.page_object.navigate_to_page(
        url=URLS["CHECKOUT_PAGE2"], title="Checkout: Overview"
    )

@when("I click 'Cancel'")
def step_click_cancel(context):
    context.page_object.cancel_checkout()

@when("I click 'Finish'")
def step_click_finish(context):
    context.page_object.finalize_payment()

@then("The page should contain correct price details")
def step_verify_order_details(context):
    context.page_object.validate_order_price_details()

@then("I should be redirected to the 'Checkout completed' page")
def step_redirect_order_complete(context):
    context.page_object.current_page_should_be(
        expected_url=URLS["CHECKOUT_PAGE3"], title="Checkout: Complete!")
    context.page_object.thank_you_heading.is_visible()
