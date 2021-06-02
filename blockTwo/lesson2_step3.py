from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


def summ(x, y):
    return str(x + y)


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = int(browser.find_element_by_id('num1').text)
    print(num1)
    num2 = int(browser.find_element_by_id('num2').text)
    print(num2)
    summa = summ(num1, num2)
    print(summa)
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(summa)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
