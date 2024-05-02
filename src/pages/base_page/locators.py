class BaseLocators:
    def __init__(self):
        self.currency_dropdown = '#currencies-block-top'
        self.current_currency = '#currencies-block-top .current strong'
        self.currency_to_select = lambda curr : f'#first-currencies li a[title="{curr}"]'
        self.language_dropdown = '#languages-block-top'
        self.current_lang = '#languages-block-top .current span'
        self.language_to_select = lambda lang : f'#first-languages li a[title="{lang}"]'