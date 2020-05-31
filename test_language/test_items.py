from selenium import webdriver
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_out_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_element_by_class_name("btn-add-to-basket")
    assert  button == button, "Element not found"