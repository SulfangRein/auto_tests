from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/execute_script.html'
browser = webdriver.Chrome()

try:
    browser.get(link)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    field = browser.find_element_by_id('answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", field)
    field.send_keys(y)

    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()

    radio = browser.find_element_by_id('robotsRule')
    radio.click()

    btn = browser.find_element_by_class_name('btn')
    btn.click()
finally:
    time.sleep(30)
    browser.quit()
