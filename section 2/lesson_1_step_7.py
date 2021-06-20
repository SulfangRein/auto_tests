from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/get_attribute.html'
browser = webdriver.Chrome()

try:
    browser.get(link)

    img = browser.find_element_by_id('treasure')
    x = img.get_attribute('valuex')

    y = calc(x)

    input = browser.find_element_by_id('answer')
    input.send_keys(y)

    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()

    radio = browser.find_element_by_id('robotsRule')
    radio.click()

    btn = browser.find_element_by_class_name('btn')
    btn.click()
finally:
    time.sleep(30)
    browser.quit()
