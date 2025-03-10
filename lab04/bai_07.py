import math 
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
ucln = math.gcd(a, b)
bcnn = abs(a * b) // ucln
print("Bội chung nhỏ nhất của", a, "và", b, "là:", bcnn)