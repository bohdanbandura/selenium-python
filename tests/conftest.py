from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.firefox.options import Options as firefox_options
from selenium.webdriver.edge.options import Options as edge_options
import pytest

@pytest.fixture(scope='module', params=['chrome', 'firefox', 'edge'])
def driver(request):
    driver = None
    
    if request.param == 'chrome':
        options = chrome_options()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
    elif request.param == 'firefox':
        options = firefox_options()
        options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)
    elif request.param == 'edge':
        options = edge_options()
        options.add_argument('--headless')
        driver = webdriver.Edge(options=options)
        
    driver.set_window_size(width=1920, height=1080)
    yield driver
    driver.quit()

