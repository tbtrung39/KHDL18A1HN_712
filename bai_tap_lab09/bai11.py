def double_factorial(n):
    if n == 0 or n == 1:
        return 1
    return double_factorial(n - 2) * n
def alternating_double_factorial_sum(k):
    if k == 0:
        return 0
    return ((-1)**k) * double_factorial(k) + alternating_double_factorial_sum(k - 1)

k = int(input("Nhập số nguyên k < 1000: "))
if k < 1000:
    print("Tổng S =", alternating_double_factorial_sum(k))
else:
    print("k phải nhỏ hơn 1000!")
