ky_tu = input("Nhập một ký tự: ")

while ky_tu == "" or (ky_tu >= " " and input("Bạn có nhập nhiều ký tự không? (Nhấn Enter nếu không): ") != ""):
    print("Vui lòng nhập một ký tự duy nhất!")
    ky_tu = input("Nhập một ký tự: ")
ascii_value = ord(ky_tu)
print("Mã ASCII của ký tự", ky_tu, "là:", ascii_value)