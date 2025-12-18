from playwright.sync_api import Page, expect


class Expects:

    def expect_to_have_text(self, locator, text):
        locator.screenshot(path=f"{locator}_{text}.png")
        expect(locator).to_have_text(text)
