str = input("Nhập chuỗi ký tự: ")
dem = 0
for c in str:
    if c.isdigit():
        dem += 1
print("Số lượng ký tự là chữ số:", dem)
