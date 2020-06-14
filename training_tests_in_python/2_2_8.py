#Открыть страницу http://suninjuly.github.io/file_input.html
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    #Заполнить текстовые поля: имя, фамилия, email
    input1=browser.find_element_by_name("firstname")
    input1.send_keys("test")
    input2=browser.find_element_by_name("lastname")
    input2.send_keys("test")
    input3=browser.find_element_by_name("email")
    input3.send_keys("test")

    #Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'test.txt') 
    element=browser.find_element_by_id("file") 
    element.send_keys(file_path)

    #Нажать кнопку "Submit"
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()