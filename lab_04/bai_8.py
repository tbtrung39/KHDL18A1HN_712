x = input("Nhập một ký tự: ")
if x!= " ":
    kytu = x[0]
    ascii_value = ord(kytu)
    print("Giá trị ASCII", kytu, "la", ascii_value)
else:
    print("không hợp lệ")