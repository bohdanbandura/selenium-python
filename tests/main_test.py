from src.pages.main_page.main_page_tests import MainPageTests
from src.pages.search_page.search_page_tests import SearchPageTests

from src.constants import BASE_URL
from src.page_factory import PageFactory

import pytest

# page_factory = PageFactory('chrome')
# driver = page_factory.driver
# main_page = page_factory.main_page
# search_page = page_factory.search_page
main_page_test = MainPageTests()
search_page_test = SearchPageTests()

@pytest.mark.usefixtures("pages")
class TestMain:
    
    def test_home_page(self, pages):
        
        driver, main_page, _ = pages
        
        main_page.open(BASE_URL)
        main_page_test.check_currency(driver, main_page)
        main_page_test.set_currency(main_page, 'Доллар')
        main_page.search_items_by_name('dress')
    
    def test_search_page(self, pages):
        
        _, main_page, search_page = pages
                
        items_displayed = search_page_test.check_items_displayed(search_page)
        search_page_test.check_currency(search_page, main_page, items_displayed)
        selected_currency_char, items_displayed = search_page_test.check_sorting(search_page)
        search_page_test.check_discount(search_page, items_displayed, selected_currency_char)
