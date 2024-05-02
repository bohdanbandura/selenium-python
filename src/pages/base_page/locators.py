class BaseLocators:
    def __init__(self):
        self.currency_dropdown = '#currencies-block-top'
        self.current_currency = '#currencies-block-top .current strong'
        self.currency_to_select = lambda curr : f'#first-currencies li a[title="{curr}"]'