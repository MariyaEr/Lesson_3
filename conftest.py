import pytest


@pytest.fixture(scope='session')
def browser():
    print('браузер')
    yield
    print ('Закрываем браузер')