password_str = input("Nhập các mật khẩu phân cách bởi dấu phẩy: ")
passwords = [p.strip() for p in password_str.split(',')]

valid_passwords = []

for p in passwords:
    if len(p) < 6 or len(p) > 12:
        continue
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    
    for c in p:
        if c.islower():
            has_lower = True
        elif c.isupper():
            has_upper = True
        elif c.isdigit():
            has_digit = True
        elif c in ['$', '#', '@']:
            has_special = True
    if has_lower and has_upper and has_digit and has_special:
        valid_passwords.append(p)
print("Mật khẩu hợp lệ:", ', '.join(valid_passwords))