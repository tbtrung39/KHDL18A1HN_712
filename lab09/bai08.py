# a.
def sum_a(n):
    if n == 1:
        return 1 / (1*2)
    return 1 / (n*(n+1)+sum_a(n-1))
n=int(input("Nhap n:"))
print("Tong S =",sum_a(n))
# b.
def factorial(n):
    if n == 0 or n==1:
        return 1 
    return n*factorial(n-1)
def sum_b(n):
    if n==0:
        return 1 
    return 1 / factorial(n)+sum_b(n-1)
n=int(input("Nhap n :"))
print("Tong S =",sum_b(n))
# c.
import math 
def nested_sqrt(n):
    if n == 1:
        return math.sqrt(3)
    return math.sqrt(3*n+nested_sqrt(n-1))
n = int(input("Nhap n:"))
print("Gia tri S=",nested_sqrt(n))
# d.
import math
def nested_sqrt(k, n):
    if k == 1:
        return math.sqrt(1)
    elif k == 2:
        return (2 + nested_sqrt(1, n)) ** (1 / n)
    elif k == n:
        return (n - 1 + nested_sqrt(n - 1, n)) ** (1 / n)
    else:
        return (k + nested_sqrt(k - 1, n)) ** (1 / n)
def compute_S(n):
    inner = nested_sqrt(n, n)
    S = (n + inner) ** (1 / (n + 1))
    return S
n = int(input("Nhập n: "))
S = compute_S(n)
print("Giá trị của S là:", S)