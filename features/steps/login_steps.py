from behave import given, when, then


@given("I am on the login page")
def step_open_login_page(context):
    context.page_object.navigate_to_login_page()

@when("I enter valid credentials and click 'Login'")
def step_enter_valid_credentials(context):
    context.page_object.login_user_success()

@then("I should be redirected without any errors")
def step_redirected_without_error(context):
    context.page_object.redirected_to_inventory_without_error()

@when("I use a username for locked account and click 'Login'")
def step_enter_locked_username(context):
    context.page_object.login_error_locked_user()

@then("I should see an error message about locked user")
def step_locked_user_error(context):
    context.page_object.expect_login_error_with_text(
        "Epic sadface: Sorry, this user has been locked out."
    )

@when("I leave the username field empty and click 'Login'")
def step_missing_username(context):
    context.page_object.login_missing_username()

@then("I should see an error message about missing username")
def step_missing_username_error(context):
    context.page_object.expect_login_error_with_text(
        "Epic sadface: Username is required"
    )

@when("I leave the password field empty and click 'Login'")
def step_missing_password(context):
    context.page_object.login_missing_password()

@then("I should see an error message about missing password")
def step_missing_password_error(context):
    context.page_object.expect_login_error_with_text(
        "Epic sadface: Password is required"
    )

@when("I enter a valid username and an incorrect password and click 'Login'")
def step_invalid_credentials(context):
    context.page_object.login_error_wrong_password()

@then("I should see an error message about invalid credentials")
def step_invalid_credentials_error(context):
    context.page_object.expect_login_error_with_text(
        "Epic sadface: Username and password do not match any user in this service"
    )
