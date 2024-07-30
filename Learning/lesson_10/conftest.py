import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    print('start browser')
    # driver передается в тесты
    yield driver
    print('\nquit browser...')
    #закрываем сессию после того как тесты прошли
    driver.quit()