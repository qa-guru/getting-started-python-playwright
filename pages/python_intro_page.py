import allure
from playwright.sync_api import Page, expect, Locator

from helpers.expects import Expects
from helpers.urls import BASE_URL


class IntroPythonPage:

    def __init__(self, page):
        self.page: Page = page
        self.expect = Expects()
        self.path = f'{BASE_URL}/python/docs/intro'

        self.link_header_python_locator: Locator = page.locator('[class="navbar__link"]')
        self.next_button_locator: Locator = page.locator('.pagination-nav__link.pagination-nav__link--next')

    @allure.step("Open page")
    def open(self):
        self.page.goto(self.path)
        self.page.wait_for_url(self.path)

    def click_on_next(self):
        self.next_button_locator.click()

    def assert_that_intro_page_is_visible(self):
        self.page.wait_for_selector('[class="navbar__link"]', timeout=30000, state='visible')
        self.expect.expect_to_have_text(self.link_header_python_locator, 'Python')

        expect(self.page).to_have_url('https://playwright.dev/python/docs/writing-tests')
        expect(self.page).to_have_title('Writing tests | Playwright Python')
