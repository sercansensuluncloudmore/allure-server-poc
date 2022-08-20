from playwright.sync_api import Page

MAIN_PAGE_URL = 'https://playwright.dev/python/'


def test_playwright_main_page_has_icon(page: Page):
    page.goto(MAIN_PAGE_URL)
    assert page.is_visible("//img[@src='/python/img/playwright-logo.svg']")


def test_playwright_main_page_has_search_button(page: Page):
    page.goto(MAIN_PAGE_URL)
    assert page.is_visible("//button[@class='DocSearch DocSearch-Button']")


def test_playwright_main_page_has_get_started_button(page: Page):
    page.goto(MAIN_PAGE_URL)
    assert page.is_visible("//a[@class='getStarted_Sjon']")
