import math
def f(x):
 numerator = -x + math.sqrt(x**2 + 4)
 denominator = 7 * math.sqrt(x**4 + 1)
 return round(numerator / denominator, 2)
x = float(input("Nhập x: "))
print(f"Giá trị của f(x): {f(x)}")