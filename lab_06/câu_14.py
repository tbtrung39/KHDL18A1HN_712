import re


password = input("Nhập mật khẩu: ")


is_valid = (
    6 <= len(password) <= 12 and
    any(c.islower() for c in password) and
    any(c.isupper() for c in password) and
    any(c.isdigit() for c in password) and
    any(c in "$#@" for c in password)
)


print("Mật khẩu hợp lệ" if is_valid else "Mật khẩu không hợp lệ")
