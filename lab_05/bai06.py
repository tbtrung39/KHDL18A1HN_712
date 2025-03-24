Str = input("Nhập chuỗi ký tự: ")
hex_char = "0123456789ABCDEFabcdef"
is_hex = all(c in hex_char for c in Str)
if is_hex:
    chuoi = int(Str, 16)
    print("Chuỗi hợp lệ trong hệ Hex. Số thập phân tương ứng:", chuoi)
else:
    print("Chuỗi không hợp lệ trong Hex")