# Câu 4. Tính ước chung và bội chung
# a) Tìm ước số chung lớn nhất (UCLN) của hai số.
# b) Tìm bội số chung nhỏ nhất (BCNN) của hai số.
# c) Kiểm tra xem hai số nhập vào có nguyên tố cùng nhau không.

import math

# a)
def ucln(a, b):
    return math.gcd(a, b)

a = int(input())
b = int(input())
print(ucln(a, b))
print()

# b)
def bcnn(a, b):
    return abs(a * b) // ucln(a, b)

a = int(input())
b = int(input())
print(bcnn(a, b))
print()

# c)
def nguyen_to_cung_nhau(a, b):
    return ucln(a, b) == 1

a = int(input())
b = int(input())
if nguyen_to_cung_nhau(a, b):
    print("Yes")
else:
    print("No")
