import time
import math
import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    # browser.implicitly_wait(10)
    yield browser
    browser.quit()

@pytest.mark.xfail
@pytest.mark.parametrize('link', [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
])
def test_guest_should_see_login_link(browser, link):
    browser.get(link)
    answer = str(math.log(int(time.time())))
    inputElem = browser.find_element_by_class_name("ember-text-area")
    button = browser.find_element_by_class_name("submit-submission")
    inputElem.send_keys(answer)
    button.click()
    textAnswer = browser.find_element_by_class_name('smart-hints__hint')
    assert textAnswer.text != 'Correct', textAnswer.text
