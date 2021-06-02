from selenium import webdriver
import time
import math


def logVal(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element_by_id('input_value').text
    logarifm = logVal(num1)
    input_elem = browser.find_element_by_id('answer')
    input_elem.send_keys(logarifm)
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()
    button = browser.find_element_by_css_selector("button.btn")
    radio = browser.find_element_by_css_selector("[value='robots']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
