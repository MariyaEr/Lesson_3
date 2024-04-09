from selene import browser, be, have

def test_search(browser_size, browser_open, window):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_incorrect(browser_open):
    browser.element('[name="q"]').should(be.blank).type('tttss33333333ss33333').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
    print('Не найдено')