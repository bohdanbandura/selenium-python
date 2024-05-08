import pytest

from src.page_factory import PageFactory

from src.constants import PROD_URL, STAGING_URL, DEV_URL

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

def pytest_addoption(parser):
    parser.addoption('--env', action='store', default='production')
    
@pytest.fixture
def base_url(request):
    if request.config.getoption("--env") == 'production':
        return PROD_URL
    elif request.config.getoption("--env") == 'staging':
        return STAGING_URL
    elif request.config.getoption("--env") == 'dev':
        return DEV_URL
    