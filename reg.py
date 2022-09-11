from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def reg(url, path, email, password, name, city, options):
    driver = webdriver.Chrome(executable_path=path, chrome_options=options)
    driver.get(url)
    driver.find_element(By.XPATH, "//a[@class='btn btn--small header__reg-btn']").click()
    driver.find_element(By.XPATH, "//input[@id='email']").send_keys(email)
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
    driver.find_element(By.XPATH, "//input[@id='name']").send_keys(name)
    driver.find_element(By.XPATH, "//input[@id='cityName']").send_keys(city)
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='cityName']").send_keys(Keys.ARROW_DOWN)
    time.sleep(1)
    driver.find_element(By.XPATH, "//span[contains(text(),'Москва')]").click()
    birthday = driver.find_element(By.XPATH, "//input[@id='js_signup-date-birth']")
    birthday.click()
    birthday.send_keys(Keys.ARROW_DOWN)
    birthday.send_keys(Keys.RETURN)
    birthday.send_keys(Keys.ARROW_DOWN)
    birthday.send_keys(Keys.RETURN)
    birthday.send_keys(Keys.ARROW_DOWN)
    birthday.send_keys(Keys.RETURN)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)
    try:
        driver.find_element(By.XPATH, "//div[@class='select__viewbox form__text-input']").click()
    except:
        driver.find_element(By.CSS_SELECTOR, ".select__viewbox.form__text-input").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//li[1]//label[1]").click()
    driver.find_element(By.CSS_SELECTOR, "#form-signup-submit").click()
    time.sleep(5)
    driver.close()
