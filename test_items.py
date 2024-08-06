from selenium.webdriver.common.by import By
import time


link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_add_to_basket(browser):
    browser.get(link)
    time.sleep(3)
    assert browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket"), "Oh noy! Button is gone!"
