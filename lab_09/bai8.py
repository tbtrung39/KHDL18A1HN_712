#a
def sum_a(n):
    if n == 1:
        return 1
    return 1/n + sum_a(n-1)

n = int(input("Nhập n: "))
print("Tổng S (a):", sum_a(n))
#b
def factorial(k):
    if k == 0 or k == 1:
        return 1
    return k * factorial(k-1)

def sum_b(n):
    if n == 1:
        return 1
    return 1/factorial(n) + sum_b(n-1)

n = int(input("Nhập n: "))
print("Tổng S (b):", sum_b(n))
#c
import math

def sum_c(n):
    if n == 1:
        return math.sqrt(3)
    return math.sqrt(3*n + sum_c(n-1))

n = int(input("Nhập n: "))
print("Tổng S (c):", sum_c(n))
#d
import math

def sum_d(n):
    if n == 1:
        return math.sqrt(1)
    return math.sqrt(n + sum_d(n-1))

n = int(input("Nhập n: "))
print("Tổng S (d):", sum_d(n))