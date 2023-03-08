import math as math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
import os

# тест на заполнение полей на форме и работа с аллертом

link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()

try:
    browser.get(link)
    browser.implicitly_wait(5)


    def foo(x):
        return str(math.log(abs(12 * math.sin(x))))


    btn_action = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
    btn_action.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    value1 = browser.find_element(By.XPATH, '//*[@id="input_value"]')
    value1 = value1.text
    answer = foo(int(value1))
    answer_field = browser.find_element(By.ID, 'answer')
    answer_field.send_keys(answer)
    btn = browser.find_element(By.TAG_NAME, 'button')
    btn.click()



except Exception as E:
    print(E)

time.sleep(10)
browser.quit()
