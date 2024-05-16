from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver

from web.resources.enums import AvailableCurrencies
from services.logger_init import init_logger
from web.services.ui_tests_logger import log_info
from web.resources.locators import BaseLocators, MainPageLocators, SearchPageLocators

import allure
        
class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.logger = init_logger('main_test')
        self.wait = WebDriverWait(self.driver, 10)
        self.base_locators = BaseLocators()
        self.main_page_locators = MainPageLocators()
        self.search_page_locators = SearchPageLocators()
        
    @log_info('PAGE {link} IS OPENING')
    @allure.step('PAGE {link} IS OPENING')
    def open(self, link: str) -> None:
        self.driver.get(link)
        
    @log_info('GETTING ELEMENT {locator}')
    @allure.step('GETTING ELEMENT {locator}')
    def get_element(self, locator: str, el: WebElement = False, selector: str = None) -> WebElement:
        if el:
            return el.find_element(By.XPATH if selector == 'xpath' else By.CSS_SELECTOR, locator)
            
        return self.driver.find_element(By.XPATH if selector == 'xpath' else By.CSS_SELECTOR, locator)
    
    @log_info('GETTING ELEMENTS {locator}')
    @allure.step('GETTING ELEMENTS {locator}')
    def get_elements(self, locator: str, el: WebElement = False, selector: str = None) -> list[WebElement]:
        if el:
            return el.find_elements(By.XPATH if selector == 'xpath' else By.CSS_SELECTOR, locator)
        
        return self.driver.find_elements(By.XPATH if selector == 'xpath' else By.CSS_SELECTOR, locator)
    
    @log_info('CLICKING ON ELEMENT {locator}')
    @allure.step('CLICKING ON ELEMENT {locator}')
    def click_on_element(self, locator: str, el: WebElement = False) -> None:
        try:
            self.get_element(locator, el).click()
            return
        except:
            element = self.get_element(locator, el)
            element = self.wait.until(EC.element_to_be_clickable((element)))
            element.click()
    
    @log_info('TYPING TEXT:"{text}" INTO ELEMENT {locator}')
    @allure.step('TYPING TEXT:"{text}" INTO ELEMENT {locator}')
    def type_into_element(self, locator: str, text: str, el: WebElement = False) -> None:
        self.get_element(locator, el).send_keys(text)
    
    @log_info('GETTING TEXT FROM ELEMENT {locator}')
    @allure.step('GETTING TEXT FROM ELEMENT {locator}')
    def get_text_from_element(self, locator: str, el: WebElement = False) -> str:
        return self.get_element(locator, el).text
        
    @allure.step("Get current currency")  
    def get_current_currency(self):
        selected_currency = self.get_text_from_element(self.base_locators.current_currency)
        return AvailableCurrencies[selected_currency].value
    
    @allure.step("Set currency to {curr}") 
    def set_currency(self, curr: str):
        self.click_on_element(self.base_locators.currency_dropdown)
        self.click_on_element(self.base_locators.currency_to_select(curr))
        expected_text = AvailableCurrencies[curr].value
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, self.base_locators.current_currency), expected_text))  
    
    