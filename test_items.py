import time
def test_addtobasket_on_dif_languages(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    #time.sleep(15)
    basket = browser.find_element_by_css_selector('.btn-add-to-basket')
    assert basket, "Кнопка \'Добавить в корзину\' не найдена!!!"


