import pytest as pytest
import selenium as selenium
import math as math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select


# тест с математической функцией, который проверяет ввод значений в поле, радиобаттон, выбор из дропдауна с методом гетатрибут и чек-бокс

link = 'https://suninjuly.github.io/selects1.html'



try:
    browser = webdriver.Chrome()
    browser.get(link)


    def select_sum(x, y):
        return str(int(x) + int(y))

    num1 = browser.find_element(By.ID, 'num1')
    num2 = browser.find_element(By.ID, 'num2')
    x = num1.text
    y = num2.text
    f_num = select_sum(x, y)
    Select(browser.find_element(By.ID, 'dropdown')).select_by_value(str(f_num))
    btn = browser.find_element(By.TAG_NAME, 'button')
    btn.click()



finally:
    time.sleep(10)
    browser.quit()