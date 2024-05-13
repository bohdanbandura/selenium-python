from pages.base_page.base_page import BasePage
import allure

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Search items by name: {name}")    
    def search_items_by_name(self, name: str) -> None:
        self.type_into_element(self.main_page_locators.search_input, name)
        self.click_on_element(self.main_page_locators.search_btn)
    