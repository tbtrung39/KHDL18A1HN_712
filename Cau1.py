# Câu 1. Kiểm tra số
# a) Nhập một số nguyên và kiểm tra xem nó có phải là số hoàn hảo không.
# b) Kiểm tra xem một số có phải là số chính phương không.
# c) Kiểm tra xem một số có phải là số Fibonacci không.

def la_so_hoan_hao(n):
    tong = sum(i for i in range(1, n) if n % i == 0)
    return tong == n
import math
def la_so_chinh_phuong(n):
    return int(math.sqrt(n)) ** 2 == n

def la_so_fibonacci(n):
    x1 = 5 * n * n + 4
    x2 = 5 * n * n - 4
    return int(math.sqrt(x1)) ** 2 == x1 or int(math.sqrt(x2)) ** 2 == x2
n = int(input("Nhập một số nguyên: "))
# a
if la_so_hoan_hao(n):
    print(f"Số {n} là số hoàn hảo.")
else:
    print(f"Số {n} không phải là số hoàn hảo.")

# b)
if la_so_chinh_phuong(n):
    print(f"Số {n} là số chính phương.")
else:
    print(f"Số {n} không phải là số chính phương.")
# c)
if la_so_fibonacci(n):
    print(f"Số {n} là số Fibonacci.")
else:
    print(f"Số {n} không phải là số Fibonacci.")
