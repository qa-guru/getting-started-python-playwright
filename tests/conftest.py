from typing import Dict, Any

import allure
import pytest
import requests
from _pytest.fixtures import FixtureRequest
from _pytest.nodes import Item
from axe_playwright_python.sync_playwright import Axe
from playwright.sync_api import Page, Playwright

@pytest.fixture(autouse=True)
def attach_playwright_results(page: Page, request: FixtureRequest):
    yield
    if request.node.rep_call.failed:
        allure.attach(
            body=page.url,
            name="URL",
            attachment_type=allure.attachment_type.URI_LIST,
        )
        allure.attach(
            page.screenshot(full_page=True),
            name="Screen shot on failure",
            attachment_type=allure.attachment_type.PNG,
        )


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item: Item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
