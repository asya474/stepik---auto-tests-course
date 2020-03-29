from selenium import webdriver
import time
import math

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    #Нажать кнопку 
    button1 = browser.find_element_by_class_name("trollface.btn.btn-primary")
    button1.click()
    time.sleep(1)

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(1)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
  
    y=math.log(abs(12*math.sin(int(x))))

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