from pages.main_page.main_page import MainPage
from pages.search_page.search_page import SearchPage
from src.constants import BASE_URL
from src.pages.main_page.tests.check_currency_home_page import check_currency_home_page
from src.pages.search_page.tests.check_items_displayed import check_items_displayed
from src.pages.search_page.tests.check_currency_search_page import check_currency_search_page
from src.pages.search_page.tests.check_sorting import check_sorting
import pytest

@pytest.mark.usefixtures("driver")
class TestMain:
    
    def test_home_page(self, driver):
        
        main_page = MainPage(driver)
        
        main_page.open(BASE_URL)
        check_currency_home_page(driver, main_page)
    
    def test_search_page(self, driver):
        
        main_page = MainPage(driver)
        search_page = SearchPage(driver)
        
        main_page.search_items_by_name('dress')
        items_displayed = check_items_displayed(search_page)
        check_currency_search_page(search_page, main_page, items_displayed)
        selected_currency_char, items_displayed = check_sorting(search_page)
        search_page.check_discount(items_displayed, selected_currency_char)
