from playwright.sync_api import sync_playwright


class BrowserFactory:
    def __init__(self, headless: bool = True):
        self.headless = headless
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    def start_execution(self):
        self.playwright = sync_playwright().start()
        self.playwright.selectors.set_test_id_attribute("data-test")
        self.browser = self.playwright.chromium.launch(headless=self.headless)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

        return self.page

    def stop_execution(self):
        self.context.close()
        self.browser.close()
        self.playwright.stop()
