from reg import reg
from get_mail import get_mail
from spam import spam
import time
import random
from selenium import webdriver

def main():
    for i in range(10000):

        with open("proxy", "r") as f:
            list_proxy = f.readlines()
            proxy = list_proxy[0].strip()

        with open("useragents", "r") as f:
            list_useragents = f.readlines()
            useragent = list_useragents[0].strip()

        with open("login", "r") as f:
            list_login = f.readlines()
            email = list_login[0].strip()

        with open("password", "r") as f:
            list_password = f.readlines()
            password = list_password[0].strip()

        with open("password", "w") as f:
            new_list = list_password[1:]
            content = "".join(new_list)
            f.write(content)

        with open("proxy", "w") as f:
            new_list = list_proxy[1:]
            content = "".join(new_list)
            f.write(content)

        with open("useragents", "w") as f:
            new_list = list_useragents[1:]
            content = "".join(new_list)
            f.write(content)

        with open("login", "w") as f:
            new_list = list_login[1:]
            content = "".join(new_list)
            f.write(content)

        url = "https://www.privetsecret.com/"
        path = "chromedriver.exe"
        options = webdriver.ChromeOptions()
        options.add_argument("no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=800,600")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument(f"--proxy-server={proxy}")
        options.add_argument('--headless')
        options.add_argument(f'user-agent={useragent}')
        name_list = ["David", "Vlad", "Ruslan", "Danil", "Mark", "Denis", "Kiril"]
        name = name_list[random.randint(0,6)]
        tg = ["sashka_mng", "vladaesc"]
        city = "Москва"
        search_url = f"https://privetsecret.com/search?tab=online&city=&cityId=&page={random.randint(0,3)}"
        spam_text = f"Т Г {tg[random.randint(0,1)]}"
        try:
            with open("log.txt", "a") as f:
                f.write("starting registration\n")
            reg(url=url, path=path, email=email, password=password, name=name, city=city, options=options)
            with open("log.txt", "a") as f:
                f.write("searching for email\n")
            activate_url = get_mail(email_account=email, password=password)
            with open("log.txt", "a") as f:
                f.write("activation email found, start sleeping\n")
            time.sleep(1800)
            with open("log.txt", "a") as f:
                f.write("starting to spam")
            spam(path=path, activate_url=activate_url, search_url=search_url, spam_text=spam_text, options=options)
        except:
            with open("log.txt", "a") as f:
                f.write("caught error")
            continue

main()
