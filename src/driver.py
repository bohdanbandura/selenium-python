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
        
        # driver.quit()