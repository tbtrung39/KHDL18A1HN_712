Str = input("Nhập chuỗi ký tự: ")
hex_chars = "0123456789ABCDEFabcdef"
hex_str = ""
for c in Str:
    if c in hex_chars:
        hex_str += c
if hex_str == "":
    print("Không có ký tự hợp lệ trong hệ Hex.")
else:
    print("Chuỗi hệ Hex:", hex_str)
    print("Giá trị thập phân:", int(hex_str, 16))
