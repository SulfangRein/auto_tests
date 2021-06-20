from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name_field = browser.find_element_by_css_selector("[placeholder='Input your first name']")
    first_name_field.send_keys("Tony")

    last_name_field = browser.find_element_by_css_selector("[placeholder='Input your last name']")
    last_name_field.send_keys("Montana")

    email_field = browser.find_element_by_css_selector("[placeholder='Input your email']")
    email_field.send_keys("test123@yopmail.com")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
