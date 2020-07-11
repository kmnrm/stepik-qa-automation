from selenium import webdriver
from math import sin, log as ln
import time

link = 'http://suninjuly.github.io/get_attribute.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)
    math_problem = browser.find_element_by_css_selector('h2 .nowrap').text
    math_problem = math_problem.split(' ')[2].replace(',', '')
    x = browser.find_element_by_id('treasure')\
        .get_attribute('valuex')
    answer = str(eval(math_problem.replace('(x)', f'({x})')))
    input_answer = browser.find_element_by_id('answer')
    input_answer.send_keys(answer)
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()
    radio = browser.find_element_by_id('robotsRule')
    radio.click()
    submit = browser.find_element_by_tag_name('button')
    submit.click()
finally:
    time.sleep(10)
    browser.quit()
