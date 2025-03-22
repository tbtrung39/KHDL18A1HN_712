# Câu 1.
Str = input("Nhập chuỗi ký tự: ")
count = 0
for c in Str:
    if '0' <= c <= '9':
        count += 1
print("Số ký tự là số trong chuỗi", count)        