from behave import given, when, then
from utils.helpers import login_cookie, fill_cart_script, URLS

@given("I'm authenticated and ready to checkout")
def step_ready_to_checkout(context):
    context.page.context.add_cookies([login_cookie()])
    context.page.context.add_init_script(script=fill_cart_script())
    context.page_object.navigate_to_page(
        url=URLS["CHECKOUT_PAGE1"], title="Checkout: Your Information"
    )

@when("I try to proceed without providing a first name")
def step_proceed_without_fn(context):
    context.page_object.proceed_to_final_checkout()

@when("I try to proceed without providing a last name")
def step_proceed_without_ln(context):
    context.page_object.fill_first_name(first_name="Testy")
    context.page_object.proceed_to_final_checkout()

@when("I try to proceed without providing a ZIP code")
def step_proceed_without_zip(context):
    context.page_object.fill_first_name(first_name="Testy")
    context.page_object.fill_last_name(last_name="McTester")
    context.page_object.proceed_to_final_checkout()

@when("I click proceed after providing all required info")
def step_proceed_with_all_info(context):
    context.page_object.fill_all_required_info_and_proceed(
        first_name="Testy",
        last_name="McTester",
        zip_code="123456"
    )

@then("I should see an error about missing first name")
def step_missing_fname_error(context):
    context.page_object.missing_info_warning(
        expected_error="Error: First Name is required"
    )

@then("I should see an error about missing last name")
def step_missing_lname_error(context):
    context.page_object.missing_info_warning(
        expected_error="Error: Last Name is required"
    )

@then("I should see an error about missing ZIP code")
def step_missing_zip_error(context):
    context.page_object.missing_info_warning(
        expected_error="Error: Postal Code is required"
    )

@then("I should be redirected to the second checkout page")
def step_redirected_to_second_checkout(context):
    context.page_object.current_page_should_be(
        expected_url=URLS["CHECKOUT_PAGE2"], title="Checkout: Overview"
    )
