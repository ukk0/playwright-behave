from playwright.sync_api import Page, expect

PAGE_URL = "https://www.saucedemo.com/"
USERNAME_SUCCESS = "standard_user"
USERNAME_LOCKED = "locked_out_user"
PASSWORD_SUCCESS = "secret_sauce"
PASSWORD_FAIL = "s3cr3ts4uc3"

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.user_name_input = page.get_by_test_id("username")
        self.user_password_input = page.get_by_test_id("password")
        self.login_button = page.get_by_test_id("login-button")
        self.login_error_message = page.get_by_test_id("error")

    def navigate_to_login_page(self):
        self.page.goto(PAGE_URL)

    def login_user(self, username: str = None, password: str = None):
        self.user_name_input.fill(username)
        self.user_password_input.fill(password)
        self.login_button.click()

    def expect_login_error_with_text(self, text: str):
        expect(self.login_error_message).to_be_visible()
        expect(self.login_error_message).to_have_text(text)

    def login_user_success(self):
        self.login_user(USERNAME_SUCCESS, PASSWORD_SUCCESS)
        expect(self.login_error_message).not_to_be_visible()
        expect(self.page).to_have_url(PAGE_URL + "inventory.html")

    def login_missing_username(self):
        self.login_user()
        self.expect_login_error_with_text("Epic sadface: Username is required")

    def login_missing_password(self):
        self.login_user(USERNAME_SUCCESS)
        self.expect_login_error_with_text("Epic sadface: Password is required")

    def login_error_locked_user(self):
        self.login_user(USERNAME_LOCKED, PASSWORD_SUCCESS)
        self.expect_login_error_with_text(
            "Epic sadface: Sorry, this user has been locked out."
        )

    def login_error_wrong_password(self):
        self.login_user(USERNAME_SUCCESS, PASSWORD_FAIL)
        self.expect_login_error_with_text(
            "Epic sadface: Username and password do not match any user in this service"
        )