import os
from time import sleep
from selenium import webdriver

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

link = 'http://suninjuly.github.io/file_input.html'
fields = ['firstname', 'lastname', 'email']

browser = webdriver.Chrome()
browser.get(link)

for field in fields:
    browser.find_element_by_css_selector(f"input[name='{field}']").send_keys('1')

browser.find_element_by_id('file').send_keys(file_path)
browser.find_element_by_class_name('btn').click()

sleep(10)
browser.quit()