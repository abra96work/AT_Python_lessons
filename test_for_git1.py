import pytest as pytest
import selenium as selenium
import math as math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# тест с математической функцией, который проверяет ввод значений в поле, радиобаттон и чек-бокс

link = 'http://suninjuly.github.io/get_attribute.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'treasure')
    elem_x = x_element.get_attribute('valuex')
    y = calc(elem_x)
    x_field = browser.find_element(By.ID, 'answer')
    x_field.send_keys(y)
    checkbox_robo = browser.find_element(By.ID, 'robotCheckbox')
    checkbox_robo.click()
    radio_check = browser.find_element(By.ID, 'robotsRule')
    radio_check.click()
    btn = browser.find_element(By.TAG_NAME, 'button')
    btn.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()