class MainPageLocators:
    def __init__(self):
        self.popular_goods = 'div[class="tab-content"] #homefeatured li'
        self.good_price = '.right-block .price'
        self.search_input = '#search_query_top'
        self.search_btn = 'button[name="submit_search"]'
        self.active_tab = '#home-page-tabs li[class="active"] a'