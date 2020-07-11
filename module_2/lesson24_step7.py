from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from math import sin, log as ln
import re

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 15)
browser.get('http://suninjuly.github.io/explicit_wait2.html')

try:
    optimal_price = browser.find_element(By.XPATH, "//p[contains(text(),'Optimal price')]").text
    optimal_price = re.search(r'\$\w+', optimal_price).group(0)
    button = browser.find_element(By.ID, 'book')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    wait.until(EC.text_to_be_present_in_element((By.ID, 'price'), optimal_price))
    browser.find_element(By.ID, 'book').click()
    solve = browser.find_element_by_id("solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", solve)
    math_problem, x = [
        selector.text
        for selector in browser.find_elements(By.CSS_SELECTOR, 'label .nowrap')
    ]
    answer = str(
        eval(
            math_problem.split(' ')[2].replace(',', '').replace('(x)', f'({x})')
        )
    )
    input_answer = browser.find_element_by_id('answer')
    input_answer.send_keys(answer)
    solve.click()

finally:
    sleep(10)
    browser.quit()
