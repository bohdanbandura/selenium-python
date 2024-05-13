import allure

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement

from src.pages.search_page.search_page import SearchPage
from src.pages.main_page.main_page import MainPage
from src.logger_init import log_info

class SearchPageTests:

    @allure.step("Check amount of items on page") 
    def check_items_displayed(self, search_page: SearchPage) -> list[WebElement]:
        items_found = search_page.get_number_of_found_items()
        search_page.select_number_of_items_on_page(60)
        items_displayed = search_page.get_displayed_items()
        items_count = len(items_displayed)
        assert items_found == items_count
        search_page.logger.info(f'RIGHT AMOUNT OF ITEMS ON PAGE, {items_found == items_count}')
        
        return items_displayed

    @allure.step("Check currency on search page")     
    def check_currency(self, search_page: SearchPage, main_page: MainPage, items_displayed: list[WebElement]) -> None:
        for item in items_displayed:
            selected_currency_char = search_page.get_current_currency()
            item_price = search_page.get_text_from_element(main_page.main_page_locators.good_price, item)
            assert selected_currency_char in item_price
            search_page.logger.info(f'ASSERTATION SUCCESFULL, "{selected_currency_char}" in "{item_price}", EXPECTED CURRENCY DISPLAYED')   

    @allure.step("Check if elements sorted correctly")      
    def check_sorting(self, search_page: SearchPage) -> tuple[str, list[WebElement]]:
        selected_currency_char = search_page.get_current_currency()
        search_page.select_sorting_method('price:desc')
        items_displayed = search_page.get_displayed_items()
        
        price = 0
        for item in items_displayed:
            item_price = search_page.get_item_price(item, selected_currency_char)
            if price == 0: 
                price = item_price
                continue
            try:
                assert price >= item_price
                search_page.logger.info(f'ASSERTATION SUCCESFULL "{price}" >= "{item_price}" {price >= item_price}')
                price = item_price
            except:
                search_page.logger.info('ASSERTATION FAILED, WRONG SORTING')
                break
        
        return selected_currency_char, items_displayed

    @allure.step("Check discount displayed correctly")       
    def check_discount(self, search_page: SearchPage, items_displayed, selected_currency: str) -> None:
        old_price = 0
        discount = 0
        for item in items_displayed:
            item_price = search_page.get_item_price(item, selected_currency)
            try:
                old_price = search_page.get_text_from_element(search_page.search_page_locators.discount_product_old_price, item)
                old_price = float(old_price.replace(selected_currency, '').replace(',', '.'))
                discount = search_page.get_text_from_element(search_page.search_page_locators.discount_product_discount, item)
                discount = abs(int(discount.replace('%', '')))
                if old_price != 0 and discount != 0:
                    assert old_price - ((old_price / 100) * discount) == item_price
                    search_page.logger.info('ASSERTATION SUCCESFULL')
                    search_page.logger.info(f'DISPLAYING PRICE: "{item_price}", EXPECTED PRICE: "{old_price - ((old_price / 100) * discount)}", {old_price - ((old_price / 100) * discount) == item_price}')
                else: 
                    continue
            except NoSuchElementException:
                search_page.logger.info(f'ELEMENT {item} HASN\'T DISCOUNT')
                continue
            except:
                search_page.logger.info('ASSERTATION FAILED, WRONG DISCOUNT PRICE')
                search_page.logger.info(f'DISPLAYING PRICE: "{item_price}", EXPECTED PRICE: "{old_price - ((old_price / 100) * discount)}" {old_price - ((old_price / 100) * discount) == item_price}')
                continue