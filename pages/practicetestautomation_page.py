from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page):
        self.page: Page = page

        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.submit_button = page.locator("#submit")
        self.error_message = page.locator("#error")
        self.login_section = page.locator("#login")

    def navigate_to_login_page(self):
        self.page.goto("https://practicetestautomation.com/practice-test-login/")

    def fill_username(self, username):
        self.username_input.fill(username)

    def fill_password(self, password):
        self.password_input.fill(password)

    def click_submit(self):
        self.submit_button.click()

    def get_error_message(self):
        return self.error_message.text_content()

    def is_error_visible(self):
        return self.error_message.is_visible()

    def login(self, username, password):
        self.fill_username(username)
        self.fill_password(password)
        self.click_submit()

    def clear_form(self):
        self.username_input.clear()
        self.password_input.clear()


class LoggedInSuccessfullyPage:
    def __init__(self, page):
        self.page = page

        self.page_title = page.locator(".post-title")
        self.success_message = page.locator("p.has-text-align-center")
        self.logout_button = page.locator(".wp-block-button__link")
        self.post_content = page.locator(".post-content")

    def verify_page_url(self):
        assert "practicetestautomation.com/logged-in-successfully/" in self.page.url
        return self

    def get_page_title(self):
        self.page_title.wait_for()
        return self.page_title.text_content()

    def get_success_message(self):
        self.success_message.wait_for()
        return self.success_message.text_content()

    def verify_success_message(self):
        message = self.get_success_message()
        assert "Congratulations" in message
        assert "successfully logged in" in message
        return self

    def click_logout(self):
        self.logout_button.wait_for()
        self.logout_button.click()

    def is_logout_button_displayed(self):
        return self.logout_button.is_visible()

    def verify_logout_button_displayed(self):
        assert self.is_logout_button_displayed()
        return self