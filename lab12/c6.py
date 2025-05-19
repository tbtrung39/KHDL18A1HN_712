def is_valid_username(username):
    return username.isalnum()
emails = []
try:
    username = input("Nhap username: ")
    if not is_valid_username(username):
        raise ValueError("username chi duoc chua chu va so,ko dau cach")
    email = username + "@companyname.com"
    emails.append(email)
    print('email hop le', email)
except ValueError as e:
    print("loi",e)