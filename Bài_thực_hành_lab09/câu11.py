def double_factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * double_factorial(n - 2)

def total_sum(k):
    if k == 0:
        return 0
    return ((-1) ** k) * double_factorial(k) + total_sum(k - 1)

k = int(input("Nhập k (<1000): "))
print("Tổng S là:", total_sum(k))
