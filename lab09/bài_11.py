def double_factorial(n):
    if n == 0 or n == 1 :
        return 1
    return n * double_factorial(n-2)

S = 0
for k in range(1,1000):
    term = ((-1)**k) * double_factorial(k)
    S+= term
print("Tổng S = ",S)