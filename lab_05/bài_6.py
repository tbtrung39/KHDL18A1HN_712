str = input("Nhập chuỗi ký tự : ")
hex_chars = "0123456789ABCDEFabcdef"
valid_hex = "".join([c for c in str if c in hex_chars])
if valid_hex == "":
    print("Không có kí tự hợp lệ trong hệ Hex.")
else:
    valid_hex = valid_hex.upper()
    print("Chuỗi hệ Hex hợp lệ là : ",valid_hex)
    decimal_Value = int(valid_hex,16)
    print("Giá trị thập phân tương ứng : ",decimal_Value)
