from src.pages.search_page.search_page import SearchPage

def check_items_displayed(search_page: SearchPage):
    items_found = search_page.get_number_of_found_items()
    search_page.select_number_of_items_on_page(60)
    items_displayed = search_page.get_displayed_items()
    items_count = len(items_displayed)
    assert items_found == items_count
    search_page.logger.info(f'RIGHT AMOUNT OF ITEMS ON PAGE, {items_found == items_count}')
    
    return items_displayed