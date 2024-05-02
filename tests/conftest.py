from selenium import webdriver
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.set_window_size(width=1920, height=1080)
    return driver

