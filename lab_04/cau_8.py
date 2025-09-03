char = input("Nhập một ký tự: ")
if len(char) != 1:
    print("Vui lòng chỉ nhập một ký tự duy nhất!")
else:
    ascii_value = ord(char)
    print(f"Giá trị ASCII của ký tự '{char}' là: {ascii_value}")