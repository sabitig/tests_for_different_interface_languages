def test_looking_for_a_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    button = len(browser.find_elements_by_xpath("//form[@id='add_to_basket_form']/button"))
    assert button > 0, '!!!НЕ НАШЕЛ!!!'

