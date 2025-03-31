import re

passwords = input("Nhập các mật khẩu (cách nhau bằng dấu phẩy): ").split(',')


valid_passwords = []

for password in passwords:
    password = password.strip()  


    if not (6 <= len(password) <= 12):
        continue

    if (re.search("[a-z]", password) and  
        re.search("[0-9]", password) and  
        re.search("[A-Z]", password) and 
        re.search("[$#@]", password)):  
        valid_passwords.append(password)

print("Mật khẩu hợp lệ:", ", ".join(valid_passwords))
