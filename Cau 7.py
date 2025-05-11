# Câu 7. Ước số và bội số
# a) Tìm ước số chung lớn nhất (UCLN) của hai số nguyên.
# b) Tìm bội số chung nhỏ nhất (BCNN) của hai số nguyên.

# a.
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a
a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))
print("Ước số chung lớn nhất là:", ucln(a, b))

# b.
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def bcnn(a, b):
    return abs(a * b) // ucln(a, b)
a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))
print("Bội số chung nhỏ nhất là:", bcnn(a, b))
