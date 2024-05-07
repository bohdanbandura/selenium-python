from src.driver import Driver
from src.pages.main_page.main_page import MainPage
from src.pages.search_page.search_page import SearchPage

class PageFactory:
    def __init__(self, browser):
        self.driver = Driver().set_up(browser)
        self.main_page = MainPage(self.driver)
        self.search_page = SearchPage(self.driver)
