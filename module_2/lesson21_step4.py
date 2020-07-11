from selenium import webdriver
from selenium.webdriver.common.by import By
from math import sin, log as ln
import time

link = 'http://suninjuly.github.io/math.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    math_problem, x = [
        selector.text
        for selector in browser.find_elements(By.CSS_SELECTOR, '.form-group .nowrap')
    ]
    math_problem = math_problem.split()[2].replace('(x)', f'({x})')
    answer = str(eval(math_problem.replace(',', '')))
    answer_input = browser.find_element(By.ID, 'answer')
    answer_input.send_keys(answer)
    robot_checkbox = browser.find_element(By.ID, 'robotCheckbox')
    robot_checkbox.click()

    robot_radio = browser.find_element(By.ID, 'robotsRule')
    robot_radio.click()

    submit = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit.click()
finally:
    time.sleep(10)
    browser.quit()
