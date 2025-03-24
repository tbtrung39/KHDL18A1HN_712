s = input("Nhập chuỗi ký tự: ")
count = 0
for c in s:
    if c.isdigit():
        count += 1
print("Số ký tự là số trong chuỗi:", count)