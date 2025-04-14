import math

def ucln(a, b):
    return math.gcd(a, b)

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("ƯCLN là:", ucln(a, b))
