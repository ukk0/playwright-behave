from playwright.sync_api import Page, expect
from utils.helpers import urls


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
        self.page.goto(urls["LOGIN_PAGE"])

    def enter_credentials_and_try_login(self, username: str = None, password: str = None):
        if username:
            self.user_name_input.fill(username)
        if password:
            self.user_password_input.fill(password)
        self.login_button.click()

    def expect_login_error_with_text(self, text: str):
        expect(self.login_error_message).to_be_visible()
        expect(self.login_error_message).to_have_text(text)

    def login_user_success(self):
        self.enter_credentials_and_try_login(
            username=USERNAME_SUCCESS,
            password=PASSWORD_SUCCESS
        )

    def login_missing_username(self):
        self.enter_credentials_and_try_login(password=PASSWORD_SUCCESS)

    def login_missing_password(self):
        self.enter_credentials_and_try_login(username=USERNAME_SUCCESS)

    def login_error_locked_user(self):
        self.enter_credentials_and_try_login(
            username=USERNAME_LOCKED,
            password=PASSWORD_SUCCESS
        )

    def login_error_wrong_password(self):
        self.enter_credentials_and_try_login(
            username=USERNAME_SUCCESS,
            password=PASSWORD_FAIL
        )

    def redirected_to_inventory_without_error(self):
        expect(self.login_error_message).not_to_be_visible()
        expect(self.page).to_have_url(urls["INVENTORY_PAGE"])
