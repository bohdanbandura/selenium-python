from src.base_page import BasePage

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def check_popular_items_currency(self, selected_currency):
        popular_content = self.get_elements('div[class="tab-content"] #homefeatured li')
        for item in popular_content:
            item_price = self.get_text_from_element('.right-block .price', item)
            assert selected_currency in item_price
            self.logger.info(f'ASSERTATION SUCCESFULL, "{selected_currency}" IN "{item_price}", EXPECTED CURRENCY DISPLAYED')
    
    def search_items_by_name(self, name):
        self.type_into_element('#search_query_top', text=name)
        self.click_on_element('button[name="submit_search"]')
    