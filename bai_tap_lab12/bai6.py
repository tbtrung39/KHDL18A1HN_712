def is_valid_username(username):
    return username.isalnum()

emails = []
try:
    username = input("Nhập username: ")
    if not is_valid_username(username):
        raise ValueError("Username chỉ được chứa chữ và số, không dấu cách.")
    email = username + "@companyname.com"
    emails.append(email)
    print("Email hợp lệ:", email)
except ValueError as e:
    print("Loi:", e)
