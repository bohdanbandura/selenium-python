class BaseLocators:
    def __init__(self):
        self.currency_dropdown = '#currencies-block-top'
        self.current_currency = '#currencies-block-top .current strong'
        self.currency_to_select = lambda curr : f'#first-currencies li a[title="{curr}"]'
        self.language_dropdown = '#languages-block-top'
        self.current_lang = '#languages-block-top .current span'
        self.language_to_select = lambda lang : f'#first-languages li a[title="{lang}"]'
        
class MainPageLocators:
    def __init__(self):
        self.popular_goods = 'div[class="tab-content"] #homefeatured li'
        self.good_price = '.right-block .price'
        self.search_input = '#search_query_top'
        self.search_btn = 'button[name="submit_search"]'
        self.active_tab = '#home-page-tabs li[class="active"] a'
        
class SearchPageLocators:
    def __init__(self):
        self.items_found_str = '#center_column h1 .heading-counter'
        self.number_of_items_on_page_dropdown = '#nb_item'
        self.number_of_items_to_select = lambda num : f'#nb_item option[value="{num}"]'
        self.product_block = '#center_column ul.product_list li.ajax_block_product'
        self.sort_dropdown = '#selectProductSort'
        self.sort_type_to_select = lambda val : f'#selectProductSort option[value="{val}"]'
        self.product_price_str = '.right-block .content_price .price'
        self.discount_product_old_price = '.right-block .old-price'
        self.discount_product_discount = '.right-block .price-percent-reduction'