Str = input("Nhập chuỗi ký tự: ")
count = 0
for c in Str:
    if not('a' <= c <= 'z' or 'A' <= c <= 'Z'):
        count += 1
print("Số ký tự không phải chữ cái tiếng anh là ")
