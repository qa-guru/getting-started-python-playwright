import pytest
from playwright.sync_api import Page

from pages.practicetestautomation_page import LoginPage, LoggedInSuccessfullyPage


@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)

@pytest.fixture
def logged_in_successfully_page(page: Page):
    return LoggedInSuccessfullyPage(page)

@pytest.mark.login
def test_login(login_page: LoginPage, logged_in_successfully_page: LoggedInSuccessfullyPage):
    login_page.navigate_to_login_page()
    login_page.login('student', 'Password123')

    logged_in_successfully_page.verify_success_message()
    logged_in_successfully_page.verify_logout_button_displayed()
    logged_in_successfully_page.verify_page_url()
