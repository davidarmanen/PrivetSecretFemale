from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import getpass, poplib
from selenium import webdriver


url = "https://www.privetsecret.com/"
driver = webdriver.Chrome("C:/bin/chromedriver.exe")

def main():
    driver.get(url)
    reg = driver.find_element_by_link_text("Зарегистрироваться")
    reg.send_keys(Keys.RETURN)
    email = driver.find_element_by_name("email")
    email.send_keys("anastasiia9mq9izn@mail.ru")
    password = driver.find_element_by_name("password")
    password.send_keys("password123")
    name = driver.find_element_by_name("name")
    name.send_keys("Vladik")
    city = driver.find_element_by_name("cityName")
    city.send_keys("Москва")
    city.send_keys(Keys.ARROW_DOWN)
    time.sleep(4)
    city1 = driver.find_element_by_class_name("select__item")
    city1.click()
    birthday = driver.find_element_by_name("birthday")
    birthday.click()
    birthday.send_keys(Keys.ARROW_DOWN)
    birthday.send_keys(Keys.RETURN)
    birthday.send_keys(Keys.RETURN)
    birthday.send_keys(Keys.RETURN)
    gender = driver.find_element_by_class_name("field-gender")
    gender.click()
    time.sleep(2)
    ch_gender = driver.find_element_by_css_selector("main.main:nth-child(3) section.signup.signup--page div.row div.column div.signup__content div.regform div.signup-container.callout.popup:nth-child(1) div.signup-container__content form.signup-form div.field-gender.float-error.text-input-wrap.select.js_select.is-active:nth-child(7) div.mCustomScrollbar.js_select-list.select__items.is-active ul:nth-child(1) li.select__item:nth-child(1) > label.select__link.js_select-link")
    ch_gender.click()
    reg_fin = driver.find_element_by_css_selector("#form-signup-submit")
    reg_fin.click()
    url1 = driver.current_url
    time.sleep(5)
    if url1 == "https://privetsecret.com/signup":
        main()
    else:
        pass

main()
