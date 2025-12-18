from playwright.sync_api import Page, expect, Locator

from helpers.settings import URLs


class TodoPage:

    def __init__(self, page: Page):
        self.page: Page = page

        self.todo_input: Locator = page.get_by_role("textbox", name="What needs to be done?")
        self.active_link: Locator = page.get_by_role("link", name="Active")
        self.completed_link: Locator = page.get_by_role("link", name="Completed")
        self.all_link: Locator = page.get_by_role("link", name="All")
    
    def open(self):
        self.page.goto(URLs.DEMO_TODOMVC.value)
    
    def add_todo_item(self, text: str):
        self.todo_input.fill(text)
        self.todo_input.press("Enter")
    
    def add_multiple_todo_items(self, items: list[str]):
        for item in items:
            self.add_todo_item(item)
    
    def get_todo_item(self, text: str) -> Locator:
        return self.page.get_by_text(text)
    
    def get_todo_list_item(self, text: str) -> Locator:
        return self.page.get_by_role("listitem").filter(has_text=text)
    
    def toggle_todo_item(self, text: str):
        self.get_todo_list_item(text).get_by_label("Toggle Todo").check()
    
    def verify_todo_item_visible(self, text: str):
        expect(self.get_todo_item(text)).to_be_visible()
    
    def verify_todo_item_exists(self, text: str):
        expect(self.page.locator("body")).to_contain_text(text)
    
    def verify_todo_item_checked(self, text: str, checked: bool = True):
        toggle_locator = self.get_todo_list_item(text).get_by_label("Toggle Todo")
        if checked:
            expect(toggle_locator).to_be_checked()
        else:
            expect(toggle_locator).not_to_be_checked()
    
    def click_todo_item(self, text: str):
        self.get_todo_item(text).click()
    
    def click_active_filter(self):
        self.active_link.click()
    
    def verify_todo_input_visible(self):
        expect(self.todo_input).to_be_visible()
    
    def verify_all_todo_items_visible(self, items: list[str]):
        for item in items:
            self.verify_todo_item_visible(item)

