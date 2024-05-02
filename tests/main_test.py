from pages.main_page.main_page import MainPage
from pages.search_page.search_page import SearchPage
from src.constants import BASE_URL
import pytest

pytest.mark.parametrize("driver", ['chrome', 'firefox', 'edge'])
def test_main(driver):
    main_page = MainPage(driver)
    search_page = SearchPage(driver)

    main_page.open(BASE_URL)
    
    active_tab = main_page.get_text_from_element(main_page.main_page_locators.active_tab).lower()
    assert active_tab == 'популярне'
    main_page.logger.info(f'POPULAR TAB IS OPENED, {active_tab == "популярне"}')
    
    selected_currency_char = main_page.get_current_currency()
    main_page.check_popular_items_currency(selected_currency_char)
    
    main_page.set_currency('Доллар')
    selected_currency = main_page.get_text_from_element(main_page.base_locators.current_currency)
    assert selected_currency == 'USD'
    main_page.logger.info('USD CURRENCY IS SELECTED')
    
    main_page.search_items_by_name('dress')
    
    items_found = search_page.get_number_of_found_items()
    search_page.select_number_of_items_on_page(60)
    items_displayed = search_page.get_displayed_items()
    items_count = len(items_displayed)
    assert items_found == items_count
    search_page.logger.info(f'RIGHT AMOUNT OF ITEMS ON PAGE, {items_found == items_count}')
    
    for item in items_displayed:
        selected_currency_char = search_page.get_current_currency()
        item_price = search_page.get_text_from_element(main_page.main_page_locators.good_price, item)
        assert selected_currency_char in item_price
        search_page.logger.info(f'ASSERTATION SUCCESFULL, "{selected_currency_char}" in "{item_price}", EXPECTED CURRENCY DISPLAYED')
        
    search_page.select_sorting_method('price:desc')
    items_displayed = search_page.get_displayed_items()
    
    search_page.check_price_desc_sorting(items_displayed, selected_currency_char)
    search_page.check_discount(items_displayed, selected_currency_char)
    