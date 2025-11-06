from playwright.sync_api import sync_playwright


class BrowserFactory:
    def __init__(
        self, browser_name: str = "chromium", headless: bool = True, slow_mo: int = 0
    ):
        self.browser_name = browser_name
        self.headless = headless
        self.slow_mo = slow_mo
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    def start_execution(self):
        self.playwright = sync_playwright().start()
        self.playwright.selectors.set_test_id_attribute("data-test")
        browser_launcher = getattr(self.playwright, self.browser_name)
        self.browser = browser_launcher.launch(
            headless=self.headless, slow_mo=self.slow_mo
        )
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

        return self.page

    def stop_execution(self):
        self.context.close()
        self.browser.close()
        self.playwright.stop()
