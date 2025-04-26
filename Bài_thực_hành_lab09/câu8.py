#a
def sum_a(n):
    if n == 1:
        return 1 / (1 * 2)
    return 1 / (n * (n + 1)) + sum_a(n - 1)

n = int(input("Nhập n: "))
print("Tổng S (Câu a) =", sum_a(n))

#b
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def sum_b(n):
    if n == 1:
        return 1 / 1
    return 1 / factorial(n) + sum_b(n - 1)

n = int(input("Nhập n: "))
print("Tổng S (Câu b) =", sum_b(n))
#c
import math


def sum_c(n):
    if n == 1:
        return math.sqrt(3)
    if n == 2:
        return math.sqrt(6 + math.sqrt(3))
    if n == 3:
        return math.sqrt(9 + math.sqrt(6 + math.sqrt(3)))
    return math.sqrt(3 * n + sum_c(n - 1))

n = int(input("Nhập n: "))
print("Tổng S (Câu c) =", sum_c(n))
#d
import math

def sum_d(n):
    if n == 1:
        return math.sqrt(1)
    return math.sqrt(n + sum_d(n - 1))

n = int(input("Nhập n: "))
print("Tổng S (Câu d) =", sum_d(n))
