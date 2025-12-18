from enum import Enum


class URLs(str, Enum):
    """ENUM для всех URL в проекте"""
    
    # Playwright.dev URLs
    PLAYWRIGHT_DEV = "https://playwright.dev"
    PLAYWRIGHT_DEV_HOME = "https://playwright.dev/"
    PLAYWRIGHT_PYTHON_INTRO = "https://playwright.dev/python/docs/intro"
    PLAYWRIGHT_PYTHON_WRITING_TESTS = "https://playwright.dev/python/docs/writing-tests"
    
    # Demo Playwright URLs
    DEMO_TODOMVC = "https://demo.playwright.dev/todomvc/#/"
    DEMO_API_MOCKING = "https://demo.playwright.dev/api-mocking"
    
    # Practice Test Automation URLs
    PRACTICE_TEST_AUTOMATION_LOGIN = "https://practicetestautomation.com/practice-test-login/"
    PRACTICE_TEST_AUTOMATION_LOGGED_IN = "practicetestautomation.com/logged-in-successfully/"
    
    # Habr URLs
    HABR_FEED = "https://habr.com/ru/feed/"


