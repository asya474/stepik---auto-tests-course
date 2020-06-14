from selenium import webdriver
import time
import unittest

class Test_Practice(unittest.TestCase):
    def test_practice1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)  
        input1 = browser.find_element_by_css_selector("[placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("[placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector("[placeholder='Input your email']")
        input3.send_keys("test@test.com")
        button = browser.find_element_by_css_selector("button.btn.btn-default")
        button.click()
        time.sleep(1)   
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Fuck you")
            
    def test_practice2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)  
        input1 = browser.find_element_by_css_selector("[placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("[placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector("[placeholder='Input your email']")
        input3.send_keys("test@test.com")
        button = browser.find_element_by_css_selector("button.btn.btn-default")
        button.click()
        time.sleep(1)   
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Fuck you")
        
if __name__ == "__main__":
    unittest.main()