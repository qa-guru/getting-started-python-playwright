from playwright.sync_api import Page, expect, Locator


class MainPage:
    def __init__(self, page):
        self.page: Page = page

        self.python_locator: Locator = page.locator(
            '//*[@id="docusaurus_skipToContent_fallback"]/main/section[1]/div/div/div[1]/div/p[3]/a[3]')
        self.link: Locator = page.get_by_role("link", name="Community")

    def click_on_python_link(self):
        self.python_locator.wait_for()
        self.python_locator.click()

    def open(self):
        url = "https://playwright.dev/"
        self.page.goto(url)
        self.page.wait_for_timeout(10000)
        self.page.wait_for_url(url, wait_until="load", timeout=30000)

    def click_on_link_community(self):
        self.link.wait_for(timeout=30000, state='visible')
        self.link.click()
