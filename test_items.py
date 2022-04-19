import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_button_on_page(browser):
    browser.get(link)
    time.sleep(10)
    button = browser.find_element_by_css_selector(".add-to-basket .btn-lg")
    assert button, "Button 'Add to basket' is not found"

