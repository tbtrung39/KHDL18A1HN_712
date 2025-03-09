char = input("Nhap mot ky tu: ")
if char != " ":
    kytu = char[0]
    ascii_value = ord(kytu)
    print("Gia tri ASCII", kytu, "la", ascii_value)
else:
    print("Ban chua nhap ky tu nao")