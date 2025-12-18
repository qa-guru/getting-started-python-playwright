import re

import allure
import pytest
from playwright.sync_api import Page, expect, Route, BrowserContext

from pages.community_page import CommunityPage
from pages.main_page import MainPage
from pages.python_intro_page import IntroPythonPage


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    page.goto("https://playwright.dev/")
    yield

# python -m pytest -m plw --headed --tracing on --screenshot on --video retain-on-failure
@pytest.mark.plw
def test_todomvc_basic_flow(page: Page) -> None:
    page.goto("https://demo.playwright.dev/todomvc/#/")

    # Поле ввода новой задачи
    new_todo = page.get_by_placeholder("What needs to be done?")

    # 1) Добавляем задачу
    new_todo.fill("Buy milk")
    new_todo.press("Enter")

    todo_item = page.get_by_role("listitem").filter(has_text="Buy milk")
    expect(todo_item).to_be_visible()

    breakpoint() # дебагинг тестов

    # 2) Отмечаем как выполненную (клик по чекбоксу)
    toggle = todo_item.locator("input.toggle")
    toggle.check()
    expect(todo_item).to_have_class(re.compile(r"\bcompleted\b"))

    # 3) Переходим на вкладку Completed и проверяем, что задача там есть
    page.get_by_role("link", name="Completed").click()
    expect(todo_item).to_be_visible()

    # 4) Очищаем выполненные и убеждаемся, что задача исчезла
    page.get_by_role("button", name="Clear completed").click()
    expect(todo_item).to_have_count(0)


def test_browser_context_args(page):
    intro_page = IntroPythonPage(page)
    intro_page.open()
    intro_page.click_on_next()
    intro_page.assert_that_intro_page_is_visible()


def test_page_object(page):
    main_page = MainPage(page)
    main_page.open()
    main_page.click_on_link_community()

    community = CommunityPage(page)
    community.expect_that_visible()


@pytest.mark.console
@allure.title("Test ConsoleMessage")
def test_read_from_console(page):
    page.on("console", lambda msg: print(msg.text))

    page.on("console", lambda msg: print(f"error: {msg.text}") if msg.type == "error" else None)

    with page.expect_console_message() as msg_info:
        page.evaluate("console.log('hello', 42, { foo: 'bar' })")
    msg = msg_info.value

    msg.args[0].json_value()
    msg.args[1].json_value()


def test_main1(page: Page):
    page.goto('https://playwright.dev/python/docs/intro')
    page.wait_for_timeout(10000)
    expect(page).to_have_title(re.compile("Playwright"))


def test_playwright_python(page: Page, context: BrowserContext):
    page.goto('https://playwright.dev')
    page.wait_for_load_state('networkidle')
    # Ждем появления ссылки и кликаем по ней
    playwright_link = page.get_by_role("link", name="Playwright: Fast and reliable")
    playwright_link.wait_for(state='visible', timeout=30000)
    playwright_link.click()
    # Ждем загрузки страницы после клика
    page.wait_for_load_state('networkidle')
    # Ищем ссылку Python в главном меню
    python_link = page.get_by_label("Main", exact=True).get_by_role("link", name="Python")
    python_link.wait_for(state='visible', timeout=30000)
    python_link.click()
    # Ждем загрузки страницы Python
    page.wait_for_load_state('networkidle')
    lst = context.pages
    print(lst)
    # Проверяем наличие логотипа Playwright
    logo_link = page.get_by_role("link", name="Playwright logo Playwright")
    logo_link.wait_for(state='visible', timeout=30000)
    expect(logo_link).to_be_visible()


URL = 'https://habr.com/ru/feed/'


def test_habr(page: Page):
    page.goto(URL)
    page.wait_for_load_state('networkidle')

    # Рекламный блок может не загрузиться или быть заблокирован, делаем проверку опциональной
    selector = '[id="adfox_169815559787254866"]'
    ad_locator = page.locator(selector)
    # Проверяем только если элемент существует, но не требуем его видимости
    # (реклама может быть заблокирована или не загружена)
    if ad_locator.count() > 0:
        try:
            ad_locator.wait_for(state='visible', timeout=5000)
        except Exception:
            pass  # Игнорируем, если реклама не загрузилась

    # Переходим к основной функциональности теста
    author_link = page.get_by_role("link", name="Как стать автором")
    author_link.wait_for(state='visible', timeout=30000)
    author_link.click()
    
    page.wait_for_load_state('networkidle')
    
    publish_link = page.get_by_role("link", name="Написать публикацию").first
    publish_link.wait_for(state='visible', timeout=30000)
    publish_link.click()
    
    page.wait_for_load_state('networkidle')
    
    auth_text = "Для просмотра этой страницы необходимо авторизоваться"
    expect(page.get_by_text(auth_text)).to_be_visible(timeout=30000)
    expect(page.get_by_role("main")).to_contain_text(auth_text)


@pytest.mark.mock
@allure.title("Test mock")
def test_mock_the_fruit_api(page: Page):
    page.goto("https://demo.playwright.dev/api-mocking")
    page.wait_for_timeout(10000)

    def handle(route: Route):
        json = [{"name": "Strawberry", "id": 21}]
        route.fulfill(json=json)

    page.route("*/**/api/v1/fruits", handle)
    page.goto("https://demo.playwright.dev/api-mocking")

    page.wait_for_timeout(10000)
    expect(page.get_by_text("Strawberry")).to_be_visible()
