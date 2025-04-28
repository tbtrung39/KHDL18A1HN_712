#cau a
def sum_a(n):
    if n == 1:
        return 1 / (1 * 2)
    return 1 / (n * (n + 1)) + sum_a(n - 1)

n = int(input("Nhập n: "))
print("Giá trị S (a) là:", sum_a(n))

#caub
def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua(n - 1)

def sum_b(n):
    if n == 1:
        return 1
    return 1 / giai_thua(n) + sum_b(n - 1)

n = int(input("Nhập n: "))
print("Giá trị S (b) là:", sum_b(n))

#cau c
import math

def sum_c(n):
    if n == 1:
        return math.sqrt(3)
    return math.sqrt(3 * n + sum_c(n - 1))

n = int(input("Nhập n: "))
print("Giá trị S (c) là:", sum_c(n))

#cau d
import math

def sum_d(n):
    if n == 1:
        return math.sqrt(1)
    return math.sqrt(n + sum_d(n-1))

n = int(input("Nhập n: "))
print("Giá trị S (d) là:", sum_d(n))