import allure
from playwright.sync_api import expect


class CommunityPage:

    def __init__(self, page):
        self.page = page

        self.python_locator = page.get_by_role("heading", name="Welcome")

    def expect_that_visible(self):
        expect(self.python_locator).to_be_visible()
        allure.attach(
            self.page.screenshot(),
            name="Screen shot on failure for visible page",
            attachment_type=allure.attachment_type.PNG,
        )
        allure.attach(
            self.page.screenshot(full_page=True),
            name="Screen shot on failure for full page",
            attachment_type=allure.attachment_type.PNG,
        )
        allure.attach(
            self.python_locator.screenshot(),
            name="Screen shot on failure for locator",
            attachment_type=allure.attachment_type.PNG,
        )



