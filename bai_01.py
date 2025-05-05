str_input = input("Bài 1 - Nhập chuỗi ký tự: ")
count = sum(1 for c in str_input if c.isdigit())
print("Số lượng ký tự là số:", count)