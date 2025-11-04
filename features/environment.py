from utils.browser_factory import BrowserFactory
from utils.config import HEADLESS
from utils.page_mapping import PAGE_OBJECTS


def before_all(context):
    factory = BrowserFactory(headless=HEADLESS)
    context.page = factory.start_execution()
    context.browser_factory = factory


def before_feature(context, feature):
    page_class = PAGE_OBJECTS.get(feature.name)
    if not page_class:
        raise ValueError(f"No page object mapped for feature: {feature.name}")
    context.page_object = page_class(context.page)


def after_all(context):
    context.browser_factory.stop_execution()
