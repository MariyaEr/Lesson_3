from selene import browser, be, have

def test_search(browser_size, browser_open, window):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_incorrect(browser_open):
    browser.element('[name="q"]').should(be.blank).type('gMvZjgрррSесв0Gcb1ErbpRtwZY4jI2о765оооpMa2xtsqWQ0y7hN5QM2A-gMEnACST66dLqгрпаKMtWYjFL2BrHfMa7dibCz2bCB3lLNfe-wgwQYKD1AkOnnIYSfa0EjvbFkK').press_enter()
    browser.element('[id="result-stats"]').should(have.text('About 0 results'))
    print('Не найдено')