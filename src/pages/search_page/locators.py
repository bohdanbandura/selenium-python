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