def is_valid_username(username):
    if " " in username:
        raise ValueError("Tên không được chứa dấu cách.")
    if not username.isalnum():
        raise ValueError("Tên chỉ được chứa chữ cái và chữ số.")
    return True

emails = []

while True:
    try:
        user = input("Nhập username (hoặc 'q' để thoát): ")
        if user.lower() == 'q':
            break
        if is_valid_username(user):
            email = user + "@companyname.com"
            emails.append(email)
            print("Đã thêm email:", email)
    except Exception as e:
        print("Lỗi:", e)

print("Danh sách email:", emails)
