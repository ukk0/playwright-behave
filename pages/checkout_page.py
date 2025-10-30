from playwright.sync_api import expect, Page
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.submit_info_button = page.get_by_test_id("continue")
        self.input_first_name = page.get_by_placeholder(text="First Name")
        self.input_last_name = page.get_by_placeholder(text="Last Name")
        self.input_zip_code = page.get_by_placeholder(text="Zip/Postal Code")
        self.error_missing_info = page.get_by_test_id("error")

        self.checkout_item_price = page.locator("[class='cart_item'] [class='inventory_item_price']")
        self.summary_subtotal_label = page.locator("[class='summary_subtotal_label']")
        self.summary_tax_label = page.locator("[class='summary_tax_label']")
        self.summary_total_label = page.locator("[class='summary_info_label summary_total_label']")
        self.finish_payment_button = page.get_by_test_id("finish")
        self.thank_you_page = page.get_by_role(role="heading", name="Thank you for your order!")
        self.return_to_shop_button = page.get_by_test_id("back-to-products")

    def fill_first_name(self, first_name: str):
        self.input_first_name.fill(first_name)

    def fill_last_name(self, last_name: str):
        self.input_last_name.fill(last_name)

    def fill_zip_code(self, zip_code: str):
        self.input_zip_code.fill(zip_code)

    def proceed_to_final_checkout(self):
        self.submit_info_button.click()

    def fill_all_required_info_and_proceed(
            self, first_name: str, last_name: str, zip_code: str
    ):
        self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        self.fill_zip_code(zip_code)
        self.proceed_to_final_checkout()

    def missing_info_warning(self, expected_error: str):
        expect(self.error_missing_info).to_have_text(expected_error)

    def finalize_payment(self):
        self.finish_payment_button.click()

    def return_to_shop(self):
        self.return_to_shop_button.click()
