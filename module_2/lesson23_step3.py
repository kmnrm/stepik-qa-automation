from selenium import webdriver
from time import sleep
from math import sin, log as ln

link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()
browser.get(link)
browser.find_element_by_class_name('btn').click()
browser.switch_to.alert.accept()

math_problem, x = [
    el.text
    for el in browser.find_elements_by_css_selector('label .nowrap')
]
answer = str(
    eval(
        math_problem.split(' ')[2].replace(',', '').replace('(x)', f'({x})')
    )
)
browser.find_element_by_class_name('form-control').send_keys(answer)
browser.find_element_by_class_name('btn').click()
sleep(10)
browser.quit()