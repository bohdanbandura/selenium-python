from typing import Tuple

from selenium.webdriver.remote.webdriver import WebDriver

import pytest

from src.page_factory import PageFactory
from src.pages.main_page.main_page import MainPage
from src.pages.search_page.search_page import SearchPage

@pytest.fixture(scope='module', params=['chrome', 'firefox', 'edge'])
def pages(request):
    page_factory = None
    main_page = None
    search_page = None
    driver = None
    
    if request.param == 'chrome':
        page_factory = PageFactory('chrome')
    elif request.param == 'firefox':
        page_factory = PageFactory('firefox')
    elif request.param == 'edge':
        page_factory = PageFactory('edge')
        
    driver = page_factory.driver
    main_page = page_factory.main_page
    search_page = page_factory.search_page
    
    yield driver, main_page, search_page

    driver.quit()