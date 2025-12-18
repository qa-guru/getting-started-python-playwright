from typing import Any

from playwright.sync_api import Page, BrowserContext


class AppStorageManager:
    def __init__(self, page: Page):
        self.page: Page = page
        self.browser_context: BrowserContext = page.context

    def get_cookies(self):
        return self.browser_context.cookies()

    def add_cookie(self, name: str, value: str, url: str) -> None:
        self.browser_context.add_cookies([{"name": name, "value": value, "url": url}])

    def delete_all_cookies(self) -> None:
        self.browser_context.clear_cookies()

    def get_local_storage_item(self, key: str) -> Any:
        return self.page.evaluate(
            """key => {
                const val = localStorage.getItem(key);
                try { return JSON.parse(val); } catch(e) { return val; }
            }""",
            key,
        )

    def clear_local_storage(self) -> None:
        self.page.evaluate("() => localStorage.clear()")

    def remove_local_storage_item(self, key: str) -> None:
        self.page.evaluate("key => localStorage.removeItem(key)", key)

    def assert_local_storage_key(self, key: str) -> Any:
        return self.page.evaluate(f"() => localStorage.getItem('{key}')")
