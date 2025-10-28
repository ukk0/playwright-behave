from playwright.sync_api import Page, expect


class NavigationPage:
    def __init__(self, page: Page):
        self.page = page

        self.hamburger_menu = page.get_by_role("button", name="Open Menu")
        self.side_menu_wrapper = page.locator("[class='bm-menu-wrap']")
        self.menu_all_items_button = page.get_by_role(role="link", name="All Items")
        self.menu_about_button = page.get_by_role(role="link", name="About")
        self.menu_logout_button = page.get_by_role(role="link", name="Logout")
        self.menu_reset_app_button = page.get_by_role(role="link", name="Reset App State")
        self.close_menu_button = page.get_by_role(role="button", name="Close Menu")

    def open_side_menu(self):
        self.hamburger_menu.click()

    def close_side_menu(self):
        self.close_menu_button.click()
