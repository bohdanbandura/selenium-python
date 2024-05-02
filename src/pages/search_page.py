from selenium.common.exceptions import NoSuchElementException
from src.base_page import BasePage

class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
    def get_number_of_found_items(self):
        items_found = self.get_text_from_element('#center_column h1 .heading-counter')
        return int(items_found.split(':')[1])
    
    def select_number_of_items_on_page(self, num):
        self.click_on_element('#nb_item')
        self.click_on_element(f'#nb_item option[value="{num}"]')
        
    def get_displayed_items(self):
        return self.get_elements('#center_column ul.product_list li.ajax_block_product')
    
    def select_sorting_method(self, val):
        self.click_on_element('#selectProductSort')
        self.click_on_element(f'#selectProductSort option[value="{val}"]')
        
    def get_item_price(self, item, selected_currency):
        item_price = self.get_text_from_element('.right-block .content_price .price', item)
        item_price = item_price.replace(selected_currency, '').replace(',', '.').split(' ')
        return float(''.join(item_price))

    def check_price_desc_sorting(self, items_displayed, selected_currency):
        price = 0
        for item in items_displayed:
            item_price = self.get_item_price(item, selected_currency)
            if price == 0: 
                price = item_price
                continue
            try:
                assert price >= item_price
                self.logger.info(f'ASSERTATION SUCCESFULL "{price}" >= "{item_price}" {price >= item_price}')
                price = item_price
            except:
                self.logger.info('ASSERTATION FAILED, WRONG SORTING')
                break
    
    def check_discount(self, items_displayed, selected_currency):
        old_price = 0
        discount = 0
        for item in items_displayed:
            item_price = self.get_item_price(item, selected_currency)
            try:
                old_price = self.get_text_from_element('.right-block .old-price', item)
                old_price = float(old_price.replace(selected_currency, '').replace(',', '.'))
                discount = self.get_text_from_element('.right-block .price-percent-reduction', item)
                discount = abs(int(discount.replace('%', '')))
                if old_price != 0 and discount != 0:
                    assert old_price - ((old_price / 100) * discount) == item_price
                    self.logger.info('ASSERTATION SUCCESFULL')
                    self.logger.info(f'DISPLAYING PRICE: "{item_price}", EXPECTED PRICE: "{old_price - ((old_price / 100) * discount)}", {old_price - ((old_price / 100) * discount) == item_price}')
                else: 
                    continue
            except NoSuchElementException:
                self.logger.info(f'ELEMENT {item} HASN\'T DISCOUNT')
                continue
            except:
                self.logger.info('ASSERTATION FAILED, WRONG DISCOUNT PRICE')
                self.logger.info(f'DISPLAYING PRICE: "{item_price}", EXPECTED PRICE: "{old_price - ((old_price / 100) * discount)}" {old_price - ((old_price / 100) * discount) == item_price}')
                continue