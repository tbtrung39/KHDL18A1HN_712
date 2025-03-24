str = input("Nhập chuỗi ký tự: ")
dem = 0
for c in str:
    if not c.isalnum():  # không phải chữ hoặc số
        dem += 1
print("Số ký tự không phải chữ cái tiếng Anh và không phải số là:", dem)
