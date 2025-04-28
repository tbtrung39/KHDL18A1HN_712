#a
def sum_a(n):
    if n == 1:
        return 1/2
    return sum_a(n-1) + 1/(n*(n+1))

n = int(input("Nhập n: "))
print("Giá trị S(a) là:", sum_a(n))

#b
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

def sum_b(n):
    if n == 1:
        return 1/(1*2)
    return sum_b(n-1) + 1/factorial(n)

n = int(input("Nhập n: "))
print("Giá trị S(b) là:", sum_b(n))

#c
import math

def sum_c(n):
    if n == 3:
        return math.sqrt(9 + math.sqrt(6 + math.sqrt(3)))
    return math.sqrt(3*n + sum_c(n-1))

n = int(input("Nhập n (>=3): "))
print("Giá trị S(c) là:", sum_c(n))

#d
import math

def sum_d(n):
    if n == 1:
        return math.sqrt(1 + math.sqrt(2 + math.sqrt(3 + math.sqrt(4))))
    return math.sqrt(n + sum_d(n-1))

n = int(input("Nhập n: "))
print("Giá trị S(d) là:", sum_d(n))