import time

from playwright.sync_api import Page, expect


PAGE_URL = "https://www.saucedemo.com/inventory.html"

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page

        self.page_subtitle = page.get_by_test_id("title")
        self.hamburger_menu = page.get_by_role("button", name="Open Menu")
        self.side_menu_wrapper = page.locator("[class='bm-menu-wrap']")
        self.menu_all_items_button = page.get_by_role(role="link", name="All Items")
        self.menu_about_button = page.get_by_role(role="link", name="About")
        self.menu_logout_button = page.get_by_role(role="link", name="Logout")
        self.menu_reset_app_button = page.get_by_role(role="link", name="Reset App State")
        self.close_menu_button = page.get_by_role(role="button", name="Close Menu")

        self.inventory_item = page.get_by_test_id("inventory-item")
        self.inventory_item_title = page.get_by_test_id("inventory-item-name")
        self.inventory_item_desc = page.get_by_test_id("inventory-item-desc")
        self.inventory_item_price = page.get_by_test_id("inventory-item-price")
        self.inventory_item_pict = page.locator("[class='inventory_item_img']")

        self.inventory_filter = page.get_by_test_id("product_sort_container")
        self.inventory_item_names = page.locator("[class='inventory_list'] [class='inventory_item_name']")
        self.inventory_item_prices = page.locator("[class='inventory_list'] [class='inventory_item_price']")
        self.add_item_to_cart = page.get_by_text(text="Add to cart")
        self.remove_item_from_cart = page.get_by_text(text="Remove")
        self.shopping_cart_items = page.locator("[class='shopping_cart_link'] [class='shopping_cart_badge']")

    def navigate_to_inventory_page(self):
        self.page.goto(PAGE_URL)
        expect(self.page_subtitle).to_have_text("Products")

    def open_side_menu(self):
        self.hamburger_menu.click()

    def close_side_menu(self):
        self.close_menu_button.click()

    def verify_inventory_item_contents(self):
        item_count = self.inventory_item.count()
        for i in range(item_count):
            expect(self.inventory_item_title.nth(i)).not_to_be_empty()
            expect(self.inventory_item_desc.nth(i)).not_to_be_empty()
            expect(self.inventory_item_price.nth(i)).not_to_be_empty()
            expect(self.inventory_item_pict.nth(i)).not_to_be_hidden()

    def use_inventory_filter(self, filter_option: str):
        self.inventory_filter.click()
        self.inventory_filter.select_option(filter_option)
        self.page.wait_for_load_state()

    def add_items_to_cart(self, amount_of_items: int):
        for i in range(amount_of_items):
            self.add_item_to_cart.nth(i).click()

    def remove_items_from_cart(self, amount_of_items: int):
        for i in range(amount_of_items):
            self.remove_item_from_cart.nth(i).click()

    def cart_item_count(self):
        item_count = self.shopping_cart_items.inner_text()
        return int(item_count)