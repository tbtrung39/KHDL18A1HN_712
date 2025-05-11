# Câu 6. Kiểm tra số Fibonacci (x là một số Fibonacci nếu 5x^2 + 4 hoặc 5x^2 - 4 là số chính phương)
# a) Kiểm tra xem một số nhập vào có thuộc dãy Fibonacci hay không.
# b) Tìm số Fibonacci thứ n trong dãy Fibonacci.

# a.
import math

def la_so_chinh_phuong(n):
    can = int(math.sqrt(n))
    return can * can == n

def la_so_fibonacci(x):
    return la_so_chinh_phuong(5 * x * x + 4) or la_so_chinh_phuong(5 * x * x - 4)
x = int(input("Nhập một số: "))
if la_so_fibonacci(x):
    print(x, "là số Fibonacci.")
else:
    print(x, "không phải là số Fibonacci.")

# b.
def fibonacci(n):
    if n <= 0:
        return "Vị trí phải lớn hơn 0"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    a, b = 0, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b
n = int(input("Nhập vị trí n: "))
print("Số Fibonacci thứ", n, "là:", fibonacci(n))
