from src.pages.main_page.main_page import MainPage

def check_currency_home_page(driver, main_page: MainPage):

    current_lang = main_page.get_text_from_element(main_page.base_locators.current_lang)
    
    if driver == 'firefox' or current_lang.title() != 'Українська':
        main_page.click_on_element(main_page.base_locators.language_dropdown)
        main_page.click_on_element(main_page.base_locators.language_to_select('Українська (Ukrainian)'))
    
    active_tab = main_page.get_text_from_element(main_page.main_page_locators.active_tab).lower()
    assert active_tab == 'популярне'
    main_page.logger.info(f'POPULAR TAB IS OPENED, {active_tab == "популярне"}')
    
    selected_currency_char = main_page.get_current_currency()
    main_page.check_popular_items_currency(selected_currency_char)
    
    main_page.set_currency('Доллар')
    selected_currency = main_page.get_text_from_element(main_page.base_locators.current_currency)
    assert selected_currency == 'USD'
    main_page.logger.info('USD CURRENCY IS SELECTED')