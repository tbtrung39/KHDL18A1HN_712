Str = input("Nhập chuỗi ký tự: ")
dem = 0
for ky_tu in Str:
    if not ky_tu.isalpha() and not ky_tu.isdigit():
        dem += 1
print("Số ký tự không phải chữ cái và không phải số là:", dem)
