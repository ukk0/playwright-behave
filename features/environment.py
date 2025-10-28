from utils.browser_factory import BrowserFactory
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.navigation_page import NavigationPage
from utils.config import HEADLESS

# from pages.checkout_page import CheckoutPage
# from pages.shopping_cart import ShoppingCartPage


def before_all(context):
    factory = BrowserFactory(headless=HEADLESS)
    context.page = factory.start_execution()
    context.browser_factory = factory

def before_feature(context, feature):
    if feature.name == "Login functionality":
        context.page_object = LoginPage(context.page)
    elif feature.name == "Inventory functionality":
        context.page_object = InventoryPage(context.page)
    elif feature.name == "Navigation functionality":
        context.page_object = NavigationPage(context.page)
    # TODO: Extend as needed.

def after_all(context):
    context.browser_factory.stop_execution()
