import math

def bcnn(a, b):
    return abs(a * b) // math.gcd(a, b)

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("BCNN là:", bcnn(a, b))
