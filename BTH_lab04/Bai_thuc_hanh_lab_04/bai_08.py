char = input("Nhap mot ky tu: ")
if char != " ":
    kytu = char[0]
    ascii = ord(kytu)
    print("Gia tri ASCII", kytu, "la", ascii)
else:
    print("Ban chua nhap ky tu nao")