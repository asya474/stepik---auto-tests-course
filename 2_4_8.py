from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    
    button1 = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button2=browser.find_element_by_id("book")
    button2.click()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
  
    y=math.log(abs(12*math.sin(int(x))))

    input1=browser.find_element_by_id("answer")
    input1.send_keys(str(y))
    button3 = browser.find_element_by_id("solve")
    button3.click()
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()