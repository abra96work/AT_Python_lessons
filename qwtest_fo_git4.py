import math as math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
import os


# тест на заполнение полей на форме и прикрепление файла в аттачменты

link = 'http://suninjuly.github.io/file_input.html'


try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)


    firstname = browser.find_element(By.XPATH, '/html/body/div/form/div/input[1]')
    firstname.send_keys('test123')
    lastname = browser.find_element(By.XPATH, '/html/body/div/form/div/input[2]')
    lastname.send_keys('test123232')
    mail = browser.find_element(By.XPATH, '/html/body/div/form/div/input[3]')
    mail.send_keys('mailtest@.ru')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "test.txt"
    file_path = os.path.join(current_dir, "test.txt")
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)
    btn = browser.find_element(By.TAG_NAME, 'button')
    btn.click()



except Exception as E:
    print(E)

time.sleep(10)
browser.quit()
