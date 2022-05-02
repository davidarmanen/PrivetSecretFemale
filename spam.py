import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def spam(path, activate_url, search_url, spam_text, options):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path=path, chrome_options=options, proxy=proxy)
    driver.get(activate_url)
    for i in range(1, 15):
        driver.get(search_url)
        time.sleep(5)
        try:
            btn = driver.find_element(By.XPATH, f"/html[1]/body[1]/main[1]/section[1]/div[1]/div[{i}]/div[1]/div[2]/div[1]/button[3]/span[1]")
        except:
            continue
        time.sleep(2)
        btn.click()
        time.sleep(0.5)
        input = driver.find_element(By.ID, "chatMessTextarea")
        xbutton = driver.find_element(By.XPATH, "/html[1]/body[1]/section[1]/div[2]/button[1]/i[1]")
        send = driver.find_element(By.XPATH, "/html[1]/body[1]/section[1]/div[3]/div[2]/table[1]/tbody[1]/tr[2]/td[1]/div[2]/div[3]/button[1]")
        time.sleep(0.5)
        input.send_keys(spam_text)
        time.sleep(0.5)
        send.click()
        time.sleep(0.5)
        try:
            xbutton.click()
        except:
            driver.get(search_url)
