str_input = input("Nhập chuỗi: ")
hex_str = ""
for char in str_input:
    if char in "0123456789ABCDEF":
        hex_str += char  
if hex_str:
    decimal_value = int(hex_str, 16)
    print("Giá trị thập phân:", decimal_value)
else:
    print("Chuỗi không chứa ký tự hợp lệ trong hệ Hex.")
