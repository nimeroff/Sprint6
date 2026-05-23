import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    #driver.get()
    yield driver
    driver.quit()