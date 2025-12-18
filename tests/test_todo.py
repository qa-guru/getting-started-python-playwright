import pytest
from playwright.sync_api import Page

from pages.todo_page import TodoPage


@pytest.mark.only
def test_new_year_checklist(page: Page) -> None:
    todo_page = TodoPage(page)
    
    # Открытие страницы
    todo_page.open()
    
    # Список позиций для новогоднего чек-листа
    new_year_items = [
        "купить ёлку",
        "купить подарки",
        "приготовить оливье"
    ]
    
    # Добавление всех позиций в чек-лист
    todo_page.add_multiple_todo_items(new_year_items)
    
    # Проверка, что все позиции добавлены и видны
    todo_page.verify_all_todo_items_visible(new_year_items)
    
    # Дополнительная проверка наличия каждой позиции на странице
    for item in new_year_items:
        todo_page.verify_todo_item_exists(item)
