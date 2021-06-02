from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    elem = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
    button = browser.find_element_by_id('book')

    if elem:
        button.click()

        number = browser.find_element_by_id('input_value').text
        result = calc(number)
        input = browser.find_element_by_id('answer')
        input.send_keys(result)
        button2 = browser.find_element_by_id("solve")
        button2.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(13)
    # закрываем браузер после всех манипуляций
    browser.quit()