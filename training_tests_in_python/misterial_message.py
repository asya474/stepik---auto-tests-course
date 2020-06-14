import pytest
from selenium import webdriver
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', [
"https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"])

class TestLogin(object):
    def test_find_out_mysteries(self, browser, link):
        link = f"{link}"
        browser.get(link)
        time.sleep(20)
        input=browser.find_element_by_class_name("textarea")
        answer = str(math.log(int(time.time()+2.7)))
        input.send_keys(answer)
        time.sleep(5)
        button=browser.find_element_by_class_name("submit-submission")
        button.click()
        time.sleep(10)
        correct_text = browser.find_element_by_class_name("smart-hints__hint")
        correct_text = correct_text.text
        assert  "Correct!" == correct_text, f"{correct_text}"