from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение для переменной x.
    x_element = browser.find_element_by_id("input_value")
    x = int(x_element.text)
       
    #Посчитать математическую функцию от x.
    y=str(math.log(abs(12*math.sin(x))))

    #Проскроллить страницу вниз.
    text_input = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", text_input)
    #Ввести ответ в текстовое поле.
    text_input.send_keys(y)
    

    #Выбрать чексбокс с роботом
    robot1=browser.find_element_by_css_selector("[for='robotCheckbox']")
    robot1.click()

    #переключить радио правелние роботов
    robot2=browser.find_element_by_css_selector("[for='robotsRule']")
    robot2.click()

    #Нажать кнопку "Submit"
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()