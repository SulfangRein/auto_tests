from selenium import webdriver
import time
import os

browser = webdriver.Chrome()

link = 'http://suninjuly.github.io/file_input.html'

try:
    browser.get(link)

    firstname_field = browser.find_element_by_name('firstname')
    firstname_field.send_keys('Tony')

    lastname_field = browser.find_element_by_name('lastname')
    lastname_field.send_keys('Stark')

    email_field = browser.find_element_by_name('email')
    email_field.send_keys('tonystark@avengers.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'text.txt')

    file_field = browser.find_element_by_id('file')
    file_field.send_keys(file_path)

    btn = browser.find_element_by_class_name('btn')
    btn.click()
finally:
    time.sleep(30)
    browser.quit()
