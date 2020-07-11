from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
link = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element_by_id('num1').text
    num2 = browser.find_element_by_id('num2').text
    numsum = int(num1) + int(num2)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(numsum))
    browser.find_element_by_tag_name('button').click()

except Exception as err:
    print(f'ERROR! {err}')
finally:
    sleep(10)
    browser.quit()