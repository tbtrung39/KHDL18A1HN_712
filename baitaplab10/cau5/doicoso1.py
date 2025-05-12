def input_and_print():
    """Nhập vào một số nguyên và in ra kết quả vừa nhập"""
    try:
        num = int(input("Nhập một số nguyên: "))
        print(f"Số vừa nhập: {num}")
        return num
    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên hợp lệ!")
        return None

def to_binary(num):
    """Chuyển đổi số nguyên sang hệ nhị phân"""
    if num is None:
        return None
    return bin(num)

def to_octal(num):
    """Chuyển đổi số nguyên sang hệ bát phân"""
    if num is None:
        return None
    return oct(num)

def to_hexadecimal(num):
    """Chuyển đổi số nguyên sang hệ thập lục phân"""
    if num is None:
        return None
    return hex(num)

def number_conversion():
    """Chương trình chính thực hiện các chuyển đổi"""
    num = input_and_print()
    if num is not None:
        print(f"Hệ nhị phân: {to_binary(num)}")
        print(f"Hệ bát phân: {to_octal(num)}")
        print(f"Hệ thập lục phân: {to_hexadecimal(num)}")