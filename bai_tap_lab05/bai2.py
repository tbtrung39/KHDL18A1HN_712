str_input = input("Nhập chuỗi ký tự: ")
count = 0
for char in str_input:
    if not ('A' <= char <= 'Z' or 'a' <= char <= 'z'):
        count += 1
print("Số ký tự không phải chữ cái tiếng Anh:", count)
