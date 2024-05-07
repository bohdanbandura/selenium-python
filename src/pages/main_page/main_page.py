from pages.base_page.base_page import BasePage

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def search_items_by_name(self, name: str) -> None:
        self.type_into_element(self.main_page_locators.search_input, text=name)
        self.click_on_element(self.main_page_locators.search_btn)
    