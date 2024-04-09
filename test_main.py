import random
import math
from selene import browser, be, have
import pytest

@pytest.fixture()
def browser_open(browser):
    browser.open('https://google.com')
    print('Открываем браузер')

def test_search():
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))