chuoi = input("Nhập chuỗi ký tự: ")
dem = 0
for ky_tu in chuoi:
    if not (ky_tu.isalpha() or ky_tu.isdigit()):
        dem += 1
print(f"Số ký tự không phải là chữ cái và không phải là chữ số là: {dem}")
