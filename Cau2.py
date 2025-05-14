# Câu 2. Dãy Fibonacci (x là một số Fibonacci nếu 5x^2 + 4 hoặc 5x^2 - 4 là số chính phương)
# a) Viết chương trình hiển thị n số Fibonacci đầu tiên.
# b) Tìm số Fibonacci thứ n trong dãy Fibonacci.
# c) Kiểm tra xem một số có thuộc dãy Fibonacci hay không.

import math

# a)
def hien_thi_fibonacci(n):
    fibo = [0, 1]
    for i in range(2, n):
        fibo.append(fibo[-1] + fibo[-2])
    return fibo

n = int(input("Nhập số lượng các số Fibonacci cần hiển thị: "))
fibonacci_numbers = hien_thi_fibonacci(n)
print(f"{n} số Fibonacci đầu tiên là: {fibonacci_numbers}")
print()

# b) 
def so_fibonacci_thu_n(n):
    fibo = [0, 1]
    for i in range(2, n):
        fibo.append(fibo[-1] + fibo[-2])
    return fibo[n-1]

n = int(input("Nhập n để tìm số Fibonacci thứ n: "))
print(f"Số Fibonacci thứ {n} là: {so_fibonacci_thu_n(n)}")
print()

# c) 
def la_so_fibonacci(n):
    x1 = 5 * n * n + 4
    x2 = 5 * n * n - 4
    return int(math.sqrt(x1)) ** 2 == x1 or int(math.sqrt(x2)) ** 2 == x2

n = int(input("Nhập một số để kiểm tra có thuộc dãy Fibonacci không: "))
if la_so_fibonacci(n):
    print(f"Số {n} thuộc dãy Fibonacci.")
else:
    print(f"Số {n} không thuộc dãy Fibonacci.")
