#Открыть страницу http://suninjuly.github.io/file_input.html
from selenium import webdriver
import time
import math

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    #Нажать кнопку 
    button1 = browser.find_element_by_class_name("btn.btn-primary")
    button1.click()
    time.sleep(1)
    confirm = browser.switch_to.alert
    confirm.accept()

    x_element=browser.find_element_by_id("input_value").text
    x=int(x_element)
    y=math.log(abs(12*math.sin(x)))
    input1=browser.find_element_by_id("answer")
    input1.send_keys(str(y))
    button2 = browser.find_element_by_class_name("btn.btn-primary")
    button2.click()
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()