from services.ui.pages.main_page.main_page import MainPage
import allure
class MainPageTests():
    
    @allure.step("Check if {selected_currency} is displayed for popular items")
    def check_popular_items_currency(self, main_page: MainPage, selected_currency):
        popular_content = main_page.get_elements(main_page.main_page_locators.popular_goods)
        for item in popular_content:
            item_price = main_page.get_text_from_element(main_page.main_page_locators.good_price, item)
            assert selected_currency in item_price
            main_page.logger.info(f'ASSERTATION SUCCESFULL, "{selected_currency}" IN "{item_price}", EXPECTED CURRENCY DISPLAYED')

    @allure.step("Check currency on main page")
    def check_currency(self, driver, main_page: MainPage):
        current_lang = main_page.get_text_from_element(main_page.base_locators.current_lang)
        
        if driver == 'firefox' or current_lang.title() != 'Українська':
            main_page.click_on_element(main_page.base_locators.language_dropdown)
            main_page.click_on_element(main_page.base_locators.language_to_select('Українська (Ukrainian)'))
        
        active_tab = main_page.get_text_from_element(main_page.main_page_locators.active_tab).lower()
        assert active_tab == 'популярне'
        main_page.logger.info(f'POPULAR TAB IS OPENED, {active_tab == "популярне"}')
        
        selected_currency_char = main_page.get_current_currency()
        self.check_popular_items_currency(main_page, selected_currency_char)
        
    @allure.step("Set {curr} currency")
    def set_currency(self, main_page: MainPage, curr):
        main_page.set_currency(curr)
        selected_currency = main_page.get_text_from_element(main_page.base_locators.current_currency)
        assert selected_currency == 'USD'
        main_page.logger.info('USD CURRENCY IS SELECTED')