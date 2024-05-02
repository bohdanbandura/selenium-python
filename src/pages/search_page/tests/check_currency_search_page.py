from src.pages.search_page.search_page import SearchPage
from src.pages.main_page.main_page import MainPage

def check_currency_search_page(search_page: SearchPage, main_page: MainPage, items_displayed):
    for item in items_displayed:
        selected_currency_char = search_page.get_current_currency()
        item_price = search_page.get_text_from_element(main_page.main_page_locators.good_price, item)
        assert selected_currency_char in item_price
        search_page.logger.info(f'ASSERTATION SUCCESFULL, "{selected_currency_char}" in "{item_price}", EXPECTED CURRENCY DISPLAYED')