from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import getpass, poplib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome("C:/bin/chromedriver.exe")
url = "https://privetsecret.com/confirm?code=f322288ded2ba9ddb474b00c249d060d18380121&utm_source=mailfire&utm_medium=email&utm_campaign=reg_email"
search_url = "https://www.privetsecret.com/search?tab=online&city=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0&cityId=3&ageMin=18&ageMax=35"
text = "тг armanendavid"

def main():
    driver.get(url)
    for i in range(1, 15):
        driver.get(search_url)
        time.sleep(5)
        try:
            btn = driver.find_element(By.XPATH, f"/html[1]/body[1]/main[1]/section[1]/div[1]/div[{i}]/div[1]/div[2]/div[1]/button[3]/span[1]")
        except:
            continue
        btn.click()
        time.sleep(0.5)
        input = driver.find_element(By.ID, "chatMessTextarea")
        xbutton = driver.find_element(By.XPATH, "/html[1]/body[1]/section[1]/div[2]/button[1]/i[1]")
        send = driver.find_element(By.XPATH, "/html[1]/body[1]/section[1]/div[3]/div[2]/table[1]/tbody[1]/tr[2]/td[1]/div[2]/div[3]/button[1]")
        time.sleep(0.5)
        input.send_keys(text)
        time.sleep(0.5)
        send.click()
        time.sleep(0.5)
        try:
            xbutton.click()
        except:
            driver.get(search_url)

main()