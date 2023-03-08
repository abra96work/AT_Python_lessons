from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


# тест на ожидание с помощью wait
link = 'http://suninjuly.github.io/explicit_wait2.html'



try:
    browser = webdriver.Chrome(executable_path=r"C:\Users\Антон Анатольевич\Desktop\chromedriver_win32\chromedriver.exe")
    browser.get(link)
    browser.implicitly_wait(15)

    def foo(x):
        return str(math.log(abs(12 * math.sin(x))))


    price = browser.find_element(By.ID, 'price')
    price_final = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    book = browser.find_element(By.ID, 'book')
    book.click()
    value1 = browser.find_element(By.ID, 'input_value')
    value1 = value1.text
    answer = foo(int(value1))
    answer_field = browser.find_element(By.ID, 'answer')
    answer_field.send_keys(answer)
    btn = browser.find_element(By.ID, 'solve')
    btn.click()




except Exception as E:
    print(E)

# time.sleep(10)
# browser.quit()