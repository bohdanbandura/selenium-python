from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.enums import AvailableCurrencies
import logging
import allure

formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
handler = logging.FileHandler('main_test.log')
logger = logging.getLogger('selenium')
logger.setLevel(logging.INFO)
handler.setFormatter(formatter)
logger.addHandler(handler)

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.logger = logger
        
    def open(self, link):
        log = f'PAGE {link} IS OPENING'
        with allure.step(log):
            self.logger.info(log)
            self.driver.get(link)
        
    def get_element(self, locator, el=False):
        log = f'GETTING ELEMENT {locator}'
        with allure.step(log):
            self.logger.info(log)
            if el:
                return el.find_element(By.CSS_SELECTOR, locator)
                
            return self.driver.find_element(By.CSS_SELECTOR, locator)
    
    def get_elements(self, locator, el=False):
        log = f'GETTING ELEMENTS {locator}'
        with allure.step(log):
            self.logger.info(log)
            if el:
                return el.find_elements(By.CSS_SELECTOR, locator)
            
            return self.driver.find_elements(By.CSS_SELECTOR, locator)
        
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
        selected_currency = self.get_text_from_element('#currencies-block-top .current strong')
        return AvailableCurrencies[selected_currency].value
    
    def set_currency(self, curr):
        self.click_on_element('#currencies-block-top')
        self.click_on_element(f'#first-currencies li a[title="{curr}"]')
        expected_text = AvailableCurrencies[curr].value
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#currencies-block-top .current strong'), expected_text))        
    
    