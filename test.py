import re

with open("email_2.txt") as f:
    text = f.read()

f = re.findall('https://privetsecret.com/confirm[\S]+', text)

f = f[0]
f = f.replace(")", "")

print(f)