
str_input = input("Nhập chuỗi: ")
hex_chars = "0123456789ABCDEFabcdef"
is_hex = True
hex_str = ""

for char in str_input:
    if char in hex_chars:
        hex_str += char.upper() 
    else:
        is_hex = False  
if is_hex:
    print("Chuỗi hợp lệ trong hệ Hex:", str_input)
else:
    decimal_value = 0
    power = 1  

    i = len(hex_str) - 1 
    while i >= 0:
        if '0' <= hex_str[i] <= '9':
            digit_value = ord(hex_str[i]) - ord('0')  
        else:
            digit_value = ord(hex_str[i]) - ord('A') + 10 
        
        decimal_value += digit_value * power
        power *= 16  
        i -= 1  

    print("Chuỗi sau khi loại bỏ ký tự không hợp lệ:", hex_str)
    print("Giá trị thập phân:", decimal_value)
