import math as math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select


# тест с математической функцией, который проверяет ввод значений в поле, радиобаттон, выбор из дропдауна с методом гетатрибут и чек-бокс
# также тест включает в себя скроллинг страницы с помощью havascript скрипта

link = 'http://suninjuly.github.io/execute_script.html'



try:
    browser = webdriver.Chrome()
    browser.get(link)


    def foo(x):
        return str(math.log(abs(12*math.sin(x))))

    num1 = browser.find_element(By.ID, 'input_value')
    num1 = browser.find_element(By.ID, 'input_value').text
    x = foo(int(num1))
    answer_field = browser.find_element(By.ID, 'answer')
    answer_field.send_keys(x)
    browser.execute_script("window.scrollBy(0, 100);")
    robo_check = browser.find_element(By.ID, 'robotCheckbox')
    robo_check.click()
    robo_robo = browser.find_element(By.ID, 'robotsRule')
    robo_robo.click()
    btn = browser.find_element(By.CLASS_NAME, 'btn')
    btn.click()


finally:
    time.sleep(10)
    browser.quit()