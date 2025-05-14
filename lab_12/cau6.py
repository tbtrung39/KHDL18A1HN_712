try:
    ten = input("Nhập tên người dùng: ")
    if not ten.isalnum():
        raise ValueError("Tên không hợp lệ.")
    email = ten + "@companyname.com"
    print("Email hợp lệ là:", email)
except ValueError as e:
    print("Lỗi:", e)