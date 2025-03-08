import math

def bcnn(a, b):
    """Hàm tìm Bội chung nhỏ nhất (BCNN)"""
    return abs(a * b) // math.gcd(a, b)

# Nhập hai số nguyên từ bàn phím
a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))

# Tính BCNN và in kết quả
print(f"BCNN của {a} và {b} là: {bcnn(a, b)}")
