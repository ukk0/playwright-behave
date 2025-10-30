from behave import given, when, then
from utils.helpers import login_cookie, fill_cart_script, URLS

@given("I'm authenticated and in final checkout")
def step_final_checkout(context):
    context.page.context.add_cookies([login_cookie()])
    context.page.context.add_init_script(script=fill_cart_script())
    context.page_object.navigate_to_page(
        URLS["CHECKOUT_PAGE2"], title="Checkout: Overview"
    )
