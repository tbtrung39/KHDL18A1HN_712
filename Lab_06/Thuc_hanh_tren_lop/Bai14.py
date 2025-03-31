passwords = input("Nhập mật khẩu (cách nhau bằng dấu phẩy): ").split(',')
ds = []

for p in passwords:
    p = p.strip()
    if not (6 <= len(p) <= 12):
        continue

    lower = upper = digit = special = False
    for c in p:
        if c.islower():
            lower = True
        elif c.isupper():
            upper = True
        elif c.isdigit():
            digit = True
        elif c in '$#@':
            special = True

    if lower and upper and digit and special:
        ds.append(p)

print("Mật khẩu hợp lệ:", ', '.join(ds))
