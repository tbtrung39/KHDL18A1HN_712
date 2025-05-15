def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def bcnn(a, b):
    return abs(a * b) // ucln(a, b)
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
print(f"Bội chung nhỏ nhất của {a} và {b} là:", bcnn(a, b))
