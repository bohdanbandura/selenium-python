from selenium import webdriver
import pytest

@pytest.fixture(scope='module', params=['chrome', 'firefox', 'edge'])
def driver(request):
    driver = None
    
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
    elif request.param == 'edge':
        driver = webdriver.Edge()
        
    driver.set_window_size(width=1920, height=1080)
    yield driver
    driver.quit()

