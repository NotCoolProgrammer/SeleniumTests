from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    img_val = browser.find_element_by_id('treasure').get_attribute('valuex')
    y = calc(img_val)
    input_elem = browser.find_element_by_id('answer')
    input_elem.send_keys(y)
    radio = browser.find_element_by_id('robotsRule')
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
