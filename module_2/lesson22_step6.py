from selenium import webdriver
from selenium.webdriver.common.by import By
from math import sin, log as ln

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)

math_problem, x = [
        selector.text
        for selector in browser.find_elements(By.CSS_SELECTOR, '.form-group .nowrap')
    ]
answer = str(
    eval(
        math_problem.split(' ')[2].replace(',', '').replace('(x)', f'({x})')
    )
)
input_answer = browser.find_element_by_id('answer')
input_answer.send_keys(answer)
check, radio = browser.find_elements_by_css_selector('.form-check-label')
browser.execute_script("return arguments[0].scrollIntoView(true);", check)
check.click()
radio.click()
button = browser.find_element_by_tag_name("button")

button.click()
assert True