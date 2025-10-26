from utils.browser_factory import BrowserFactory
from utils.config import HEADLESS

def before_all(context):
    factory = BrowserFactory(headless=HEADLESS)
    context.page = factory.start_execution()
    context.browser_factory = factory

def after_all(context):
    context.browser_factory.stop_execution()
