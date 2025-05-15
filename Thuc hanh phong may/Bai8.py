#a
def tinh_S_a(n):
    if n == 1:
        return 1 / (1 * 2)
    return 1 / (n * (n + 1)) + tinh_S_a(n - 1)

# Nhập và in kết quả
n = int(input("Nhập n: "))
print(f"S = {tinh_S_a(n)}")
#b
def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua(n - 1)

def tinh_S_b(n):
    if n == 1:
        return 1 / giai_thua(1)
    return 1 / giai_thua(n) + tinh_S_b(n - 1)

# Nhập và in kết quả
n = int(input("Nhập n: "))
print(f"S = {tinh_S_b(n)}")

#c
import math

def tinh_S_c(n):
    if n == 1:
        return math.sqrt(3)
    return math.sqrt(3 * n + tinh_S_c(n - 1))

# Nhập và in kết quả
n = int(input("Nhập n: "))
print(f"S = {tinh_S_c(n)}")
#d
import math

def tinh_S_d(n):
    if n == 1:
        return math.sqrt(1)
    return math.sqrt(n + tinh_S_d(n - 1))

# Nhập và in kết quả
n = int(input("Nhập n: "))
print(f"S = {tinh_S_d(n)}")
