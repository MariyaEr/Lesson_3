import pytest


@pytest.fixture()
def window():
    print('браузер')
    yield
    print ('Закрываем браузер')

