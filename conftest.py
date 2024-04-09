import pytest
from selenium import webdriver
from selene import browser

@pytest.fixture()
def window():
    print('браузер')
    yield
    print('Закрываем браузер')


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
