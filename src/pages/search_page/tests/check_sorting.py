from src.pages.search_page.search_page import SearchPage

def check_sorting(search_page: SearchPage):
    selected_currency_char = search_page.get_current_currency()
    search_page.select_sorting_method('price:desc')
    items_displayed = search_page.get_displayed_items()
    
    search_page.check_price_desc_sorting(items_displayed, selected_currency_char)
    
    return selected_currency_char, items_displayed