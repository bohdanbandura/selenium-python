import pytest
import allure
import os

from datetime import datetime

from web.services.page_factory import PageFactory

from web.resources.constants import PROD_URL, STAGING_URL, DEV_URL

@pytest.fixture(scope='module', params=['chrome', 'firefox', 'edge'])
@allure.title("Prepare pages for the test")
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
@allure.title("Running scripts depends on environment")
def base_url(request):
    if request.config.getoption("--env") == 'production':
        return PROD_URL
    elif request.config.getoption("--env") == 'staging':
        return STAGING_URL
    elif request.config.getoption("--env") == 'dev':
        return DEV_URL

@pytest.fixture(autouse=True)
@allure.title("Making screenshots on failure")
def take_creenshot_on_failure(request):
    yield
    item = request.node
    driver, _, _ = item.funcargs['pages']
    if item.rep_call.failed:
        if not os.path.isdir('failed_screenshots'):
            os.mkdir('failed_screenshots')
        driver.save_screenshot(f'./failed_screenshots/{item.name}_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.png')

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):    
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

def pytest_collection_modifyitems(items, config):
    for item in items:
        if('test_home_page' in item.name):
            item.add_marker(pytest.mark.high_priority)
        else:
            item.add_marker(pytest.mark.low_priority)