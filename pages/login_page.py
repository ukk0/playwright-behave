from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from utils.helpers import URLS, LOGIN


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.user_name_input = page.get_by_test_id("username")
        self.user_password_input = page.get_by_test_id("password")
        self.login_button = page.get_by_test_id("login-button")
        self.login_error_message = page.get_by_test_id("error")

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
            username=LOGIN["USERNAME_SUCCESS"],
            password=LOGIN["PASSWORD_SUCCESS"]
        )

    def login_missing_username(self):
        self.enter_credentials_and_try_login(password=LOGIN["PASSWORD_SUCCESS"])

    def login_missing_password(self):
        self.enter_credentials_and_try_login(username=LOGIN["USERNAME_SUCCESS"])

    def login_error_locked_user(self):
        self.enter_credentials_and_try_login(
            username=LOGIN["USERNAME_LOCKED"],
            password=LOGIN["PASSWORD_SUCCESS"]
        )

    def login_error_wrong_password(self):
        self.enter_credentials_and_try_login(
            username=LOGIN["USERNAME_SUCCESS"],
            password=LOGIN["PASSWORD_FAIL"]
        )

    def redirected_to_inventory_without_error(self):
        expect(self.login_error_message).not_to_be_visible()
        self.current_page_should_be(URLS["INVENTORY_PAGE"])
