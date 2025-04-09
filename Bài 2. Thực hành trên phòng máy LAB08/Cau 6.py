# Cau 6.

def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def bcnn(a, b):
    return abs(a * b) // ucln(a, b)
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
print("Bội chung nhỏ nhất là:", bcnn(a, b))
