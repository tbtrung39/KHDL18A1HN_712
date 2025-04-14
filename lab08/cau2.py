import math

def ucln(a, b):
    return math.gcd(a, b)

a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
print("UCLN:", ucln(a, b))