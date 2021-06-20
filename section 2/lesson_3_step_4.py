from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/alert_accept.html'


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser.get(link)
    btn = browser.find_element_by_class_name('btn')
    btn.click()

    alert = browser.switch_to.alert.accept()

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    field = browser.find_element_by_id('answer')
    field.send_keys(y)

    submit_btn = browser.find_element_by_class_name('btn-primary')
    submit_btn.click()
finally:
    time.sleep(30)
    browser.quit()
