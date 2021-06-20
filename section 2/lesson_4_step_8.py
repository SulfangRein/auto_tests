import math

from selenium import webdriver
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/explicit_wait2.html'

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser.get(link)
    book_btn = browser.find_element_by_id('book')

    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    book_btn.click()

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    field = browser.find_element_by_id('answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", field)
    field.send_keys(y)

    submit_btn = browser.find_element_by_id('solve')
    submit_btn.click()
finally:
    time.sleep(30)
    browser.quit()