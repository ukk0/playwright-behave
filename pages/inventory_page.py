from playwright.sync_api import Page, expect
from utils.helpers import urls


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page

        self.page_subtitle = page.get_by_test_id("title")
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
        self.shopping_cart_badge = page.get_by_test_id("shopping-cart-link")

    def navigate_to_inventory_page(self):
        self.page.goto(urls["INVENTORY_PAGE"])
        expect(self.page_subtitle).to_have_text("Products")

    def open_shopping_cart(self):
        self.shopping_cart_badge.click()
        expect(self.page_subtitle).to_have_text("Your Cart")

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