from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    text_elem = browser.find_element_by_id('input_value').text
    y = calc(text_elem)
    input_elem = browser.find_element_by_id('answer')
    input_elem.send_keys(y)
    radio = browser.find_element_by_css_selector("[value='robots']")
    radio.click()
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
