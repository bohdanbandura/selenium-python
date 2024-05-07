from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver

from src.enums import AvailableCurrencies
from src.logger_init import init_logger
from src.locators import BaseLocators, MainPageLocators, SearchPageLocators

import allure
        
class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.logger = init_logger()
        self.base_locators = BaseLocators()
        self.main_page_locators = MainPageLocators()
        self.search_page_locators = SearchPageLocators()
        
    def open(self, link: str) -> None:
        log = f'PAGE {link} IS OPENING'
        with allure.step(log):
            self.logger.info(log)
            self.driver.get(link)
        
    def get_element(self, locator: str, el: WebElement = False, selector: str = None) -> WebElement:
        log = f'GETTING ELEMENT {locator}'
        with allure.step(log):
            self.logger.info(log)
            if el:
                return el.find_element(By.XPATH if selector == 'xpath' else By.CSS_SELECTOR, locator)
                
            return self.driver.find_element(By.XPATH if selector == 'xpath' else By.CSS_SELECTOR, locator)
    
    def get_elements(self, locator: str, el: WebElement = False, selector: str = None) -> list[WebElement]:
        log = f'GETTING ELEMENTS {locator}'
        with allure.step(log):
            self.logger.info(log)
            if el:
                return el.find_elements(By.XPATH if selector == 'xpath' else By.CSS_SELECTOR, locator)
            
            return self.driver.find_elements(By.XPATH if selector == 'xpath' else By.CSS_SELECTOR, locator)
        
    def click_on_element(self, locator: str, el: WebElement = False) -> None:
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
        
    def type_into_element(self, locator: str, text: str, el: WebElement = False) -> None:
        log = f'TYPING TEXT:"{text}" INTO ELEMENT {locator}'
        with allure.step(log):
            self.logger.info(log)
            self.get_element(locator, el).send_keys(text)
        
    def get_text_from_element(self, locator: str, el: WebElement = False) -> str:
        log = f'GETTING TEXT FROM ELEMENT {locator}'
        with allure.step(log):
            self.logger.info(log)
            return self.get_element(locator, el).text
        
    def get_current_currency(self):
        selected_currency = self.get_text_from_element(self.base_locators.current_currency)
        return AvailableCurrencies[selected_currency].value
    
    def set_currency(self, curr: str):
        self.click_on_element(self.base_locators.currency_dropdown)
        self.click_on_element(self.base_locators.currency_to_select(curr))
        expected_text = AvailableCurrencies[curr].value
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, self.base_locators.current_currency), expected_text))  
    
    