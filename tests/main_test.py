import pytest
from typing import Tuple

from src.pages.main_page.main_page_tests import MainPageTests
from src.pages.search_page.search_page_tests import SearchPageTests
from src.pages.main_page.main_page import MainPage
from src.pages.search_page.search_page import SearchPage

from selenium.webdriver.remote.webdriver import WebDriver

main_page_test = MainPageTests()
search_page_test = SearchPageTests()

@pytest.mark.usefixtures("pages")
class TestMain:
    
    def test_home_page(self, pages: Tuple[WebDriver, MainPage, SearchPage], base_url):
        
        driver, main_page, _ = pages

        main_page.open(base_url)
        main_page_test.check_currency(driver, main_page)
        main_page_test.set_currency(main_page, 'Доллар')
        main_page.search_items_by_name('dress')
    
    def test_search_page(self, pages: Tuple[WebDriver, MainPage, SearchPage]):
        
        _, main_page, search_page = pages
                
        items_displayed = search_page_test.check_items_displayed(search_page)
        search_page_test.check_currency(search_page, main_page, items_displayed)
        selected_currency_char, items_displayed = search_page_test.check_sorting(search_page)
        search_page_test.check_discount(search_page, items_displayed, selected_currency_char)
