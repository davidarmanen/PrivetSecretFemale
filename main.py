from reg import registration
from get_mail import get_mail
from spam import spam
import time
import random
from datetime import datetime

def main():
    with open("log.txt", "w") as infotxt:
        for i in range(100):
            infotxt.write(f"start loop: {str(i)}\n")
            url = "https://www.privetsecret.com/"
            path = "C:/Users/Admin/chromedriver/chromedriver.exe"
            name_list = ["David", "Vlad", "Ruslan", "Danil", "Mark", "Denis", "Kiril"]
            name = name_list[random.randint(0,6)]
            city = "Moscow"
            search_url = f"https://privetsecret.com/search?tab=online&city=&cityId=&page={random.randint(0,3)}"
            tg = ["davidarmanin", "fentypuma"]
            spam_text = f"Т Г {tg[random.randint(0,1)]}"

            try:
                with open("login", "r") as f:
                    list_login = f.readlines()
                    email = list_login[0].strip()

                with open("password", "r") as f:
                    list_password = f.readlines()
                    password = list_password[0].strip()

                with open("login", "w") as f:
                    new_list = list_login[1:]
                    content = "".join(new_list)
                    f.write(content)

                with open("password", "w") as f:
                    new_list = list_password[1:]
                    content = "".join(new_list)
                    f.write(content)
                infotxt.write("start reg\n")
                registration(url=url, path=path, email=email, password=password, name=name, city=city)
                infotxt.write("reg success\nstart mail\n")
                activate_url = get_mail(email_account=email, password=password)
                infotxt.write("mail success\nstart spam\n")
                time.sleep(900)
                spam(path=path, activate_url=activate_url, search_url=search_url, spam_text=spam_text)

            except:
                infotxt.write("end loop\n")
                continue

main()
