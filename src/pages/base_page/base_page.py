from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.enums import AvailableCurrencies
from pages.main_page.locators import MainPageLocators
from pages.search_page.locators import SearchPageLocators
from src.pages.base_page.locators import BaseLocators
from src.logger_init import init_logger
import allure
        
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.logger = init_logger()
        self.base_locators = BaseLocators()
        self.main_page_locators = MainPageLocators()
        self.search_page_locators = SearchPageLocators()
        
    def open(self, link):
        log = f'PAGE {link} IS OPENING'
        with allure.step(log):
            self.logger.info(log)
            self.driver.get(link)
        
    def get_element(self, locator, el=False, selector=None):
        log = f'GETTING ELEMENT {locator}'
        with allure.step(log):
            self.logger.info(log)
            if el:
                return el.find_element(By.XPATH if selector == 'xpath' else By.CSS_SELECTOR, locator)
                
            return self.driver.find_element(By.XPATH if selector == 'xpath' else By.CSS_SELECTOR, locator)
    
    def get_elements(self, locator, el=False, selector=None):
        log = f'GETTING ELEMENTS {locator}'
        with allure.step(log):
            self.logger.info(log)
            if el:
                return el.find_elements(By.XPATH if selector == 'xpath' else By.CSS_SELECTOR, locator)
            
            return self.driver.find_elements(By.XPATH if selector == 'xpath' else By.CSS_SELECTOR, locator)
        
    def click_on_element(self, locator, el=False):
        log = f'CLICKING ON ELEMENT {locator}'
        with allure.step(log):
            self.logger.info(log)
            try:
                self.get_element(locator, el).click()
                return
            except:
                element = self.get_element(locator, el)
                element = self.wait.until(EC.element_to_be_clickable((element)))
                element.click()
        
    def type_into_element(self, locator, text, el=False):
        log = f'TYPING TEXT:"{text}" INTO ELEMENT {locator}'
        with allure.step(log):
            self.logger.info(log)
            self.get_element(locator, el).send_keys(text)
        
    def get_text_from_element(self, locator, el=False) -> str:
        log = f'GETTING TEXT FROM ELEMENT {locator}'
        with allure.step(log):
            self.logger.info(log)
            return self.get_element(locator, el).text
        
    def get_current_currency(self):
        selected_currency = self.get_text_from_element(self.base_locators.current_currency)
        return AvailableCurrencies[selected_currency].value
    
    def set_currency(self, curr):
        self.click_on_element(self.base_locators.currency_dropdown)
        self.click_on_element(self.base_locators.currency_to_select(curr))
        expected_text = AvailableCurrencies[curr].value
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, self.base_locators.current_currency), expected_text))  
    
    