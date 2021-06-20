from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/selects1.html'

try:
    browser.get(link)

    num1 = browser.find_element_by_id('num1')
    num2 = browser.find_element_by_id('num2')

    x = int(num1.text)
    y = int(num2.text)

    z = x + y

    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_value(str(z))

    btn = browser.find_element_by_class_name('btn')
    btn.click()
finally:
    time.sleep(5)
    browser.quit()
