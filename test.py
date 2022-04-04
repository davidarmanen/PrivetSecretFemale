import time

with open("log.txt", "w") as log:
    for i in range(10):
        try:
            time.sleep(1)
            print(i)
            log.write(str(i))
        except:
            continue