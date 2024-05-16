from selenium.webdriver.remote.webelement import WebElement

import allure

from web.services.pages.base_page.base_page import BasePage

class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step("Get number of items on search page")
    def get_number_of_found_items(self) -> int:
        items_found = self.get_text_from_element(self.search_page_locators.items_found_str)
        return int(items_found.split(':')[1])
    
    @allure.step("Set number of items on search page {num}")
    def select_number_of_items_on_page(self, num: int) -> None:
        self.click_on_element(self.search_page_locators.number_of_items_on_page_dropdown)
        self.click_on_element(self.search_page_locators.number_of_items_to_select(num))

    @allure.step("Get displayed items on search page")           
    def get_displayed_items(self) -> list[WebElement]:
        return self.get_elements(self.search_page_locators.product_block)
    
    @allure.step("Set sorting method {val}")   
    def select_sorting_method(self, val: str) -> None:
        self.click_on_element(self.search_page_locators.sort_dropdown)
        self.click_on_element(self.search_page_locators.sort_type_to_select(val))
        
    @allure.step("Get price from item")   
    def get_item_price(self, item: WebElement, selected_currency: str) -> float:
        item_price = self.get_text_from_element(self.search_page_locators.product_price_str, item)
        item_price = item_price.replace(selected_currency, '').replace(',', '.').split(' ')
        return float(''.join(item_price))