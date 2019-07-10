from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

# Нажать на кнопку
btn = browser.find_element_by_css_selector(".btn-primary").click()

# Принять confirm
confirm = browser.switch_to.alert
confirm.accept()

# На новой странице решить капчу для роботов, чтобы получить число с ответом
x = browser.find_element_by_id("input_value")
x1 = x.text

#Посчитать математическую функцию от x
def calc(x1):
  return str(math.log(abs(12*math.sin(int(x1)))))

y = calc(x1)

inp = browser.find_element_by_id("answer")
inp.send_keys(y)

btn = browser.find_element_by_css_selector(".btn-primary").click()

time.sleep(5)
browser.quit()
