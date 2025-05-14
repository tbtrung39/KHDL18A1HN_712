import re

danh_sach = []

while True:
    email = input("Nhập email (hoặc '0' để thoát): ")
    if email == '0':
        break
    try:
        if not email.endswith("@companyname.com"):
            raise ValueError("Email không thuộc công ty.")
        
        username = email.split("@")[0]
        if not re.match("^[a-zA-Z0-9]+$", username):
            raise ValueError("Username không hợp lệ.")
        
        danh_sach.append(email)
        print("Email hợp lệ và đã được lưu.")
    except ValueError as e:
        print("Lỗi:", e)

print("Danh sách email đã nhập:", danh_sach)
