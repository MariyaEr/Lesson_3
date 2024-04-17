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
    browser.open('https://google.com/ncr')
    print('Открываем браузер')


@pytest.fixture()
def browser_size():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1000,1000")
    browser.config.driver_options = options
    print('Размер браузера')
