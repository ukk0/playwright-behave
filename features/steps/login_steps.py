from behave import given, when, then
from utils.helpers import URLS


@given("I am on the login page")
def step_open_login_page(context):
    context.page_object.navigate_to_page(url=URLS["LOGIN_PAGE"])

@when("I enter valid credentials and click 'Login'")
def step_enter_valid_credentials(context):
    context.page_object.login_user_success()

@when("I use a username for locked account and click 'Login'")
def step_enter_locked_username(context):
    context.page_object.login_error_locked_user()

@when("I leave the username field empty and click 'Login'")
def step_missing_username(context):
    context.page_object.login_missing_username()

@when("I leave the password field empty and click 'Login'")
def step_missing_password(context):
    context.page_object.login_missing_password()

@when("I enter a valid username and an incorrect password and click 'Login'")
def step_invalid_credentials(context):
    context.page_object.login_error_wrong_password()

@when("I try to navigate to the inventory page without logging in")
def step_try_to_navigate_to_inventory(context):
    context.page_object.navigate_to_page(url=URLS["INVENTORY_PAGE"])

@then("I should be redirected without any errors")
def step_redirected_without_error(context):
    context.page_object.redirected_to_inventory_without_error()

@then("I should see an error message about locked user")
def step_locked_user_error(context):
    context.page_object.expect_login_error_with_text(
        text="Epic sadface: Sorry, this user has been locked out."
    )

@then("I should see an error message about missing username")
def step_missing_username_error(context):
    context.page_object.expect_login_error_with_text(
        text="Epic sadface: Username is required"
    )

@then("I should see an error message about missing password")
def step_missing_password_error(context):
    context.page_object.expect_login_error_with_text(
        text="Epic sadface: Password is required"
    )

@then("I should see an error message about invalid credentials")
def step_invalid_credentials_error(context):
    context.page_object.expect_login_error_with_text(
        text="Epic sadface: Username and password do not match any user in this service"
    )

@then("I should see an error message about required login")
def step_login_required_error(context):
    context.page_object.expect_login_error_with_text(
        text="Epic sadface: You can only access '/inventory.html' when you are logged in."
    )
