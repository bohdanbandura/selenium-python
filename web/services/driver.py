from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.firefox.options import Options as firefox_options
from selenium.webdriver.edge.options import Options as edge_options

class Driver: 
    def set_up(self, browser: str):
        driver = None
        
        if browser == 'chrome':
            options = chrome_options()
            options.add_argument('--headless')
            driver = webdriver.Chrome(options=options)
        elif browser == 'firefox':
            options = firefox_options()
            options.add_argument('--headless')
            driver = webdriver.Firefox(options=options)
        elif browser == 'edge':
            options = edge_options()
            options.add_argument('--headless')
            driver = webdriver.Edge(options=options)
            
        driver.maximize_window()
    
        return driver
        

class GridDriver:
    def set_up(self, browser: str):
        driver = None
        options = None
        
        if browser == 'chrome':
            options = chrome_options()
            options.add_argument('--headless')
        elif browser == 'firefox':
            options = firefox_options()
            options.add_argument('--headless')
        elif browser == 'edge':
            options = edge_options()
            options.add_argument('--headless')
            
        driver = webdriver.Remote(
            command_executor='http://192.168.0.42:4444',
            options=options
        )
        
        driver.maximize_window()
    
        return driver