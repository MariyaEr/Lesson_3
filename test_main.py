from selene import browser, be, have
import pytest
from selenium import webdriver

@pytest.fixture()
def browser_open():
    browser.open('https://google.com')
    print('Открываем браузер')

@pytest.fixture()
def browser_size():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=300,300")
    browser.config.driver_options = options
    print('Размер браузера')

def test_search(browser_size, browser_open, window):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_incorrect(browser_open):
    browser.element('[name="q"]').should(be.blank).type('tttss33333333ss33333').press_enter()
    browser.element('[class="mnr-c"]').should(have.text('ничего не найдено.'))
    print('Не найдено')