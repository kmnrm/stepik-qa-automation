from selenium import webdriver
import time

links = [
        'http://suninjuly.github.io/registration1.html',
        'http://suninjuly.github.io/registration2.html'
    ]

try:
    for link in links:
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector("input[required].form-control.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("input[required].form-control.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector("input[required].form-control.third")
        input3.send_keys("a@a.us")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text
        time.sleep(2)
        browser.close()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
