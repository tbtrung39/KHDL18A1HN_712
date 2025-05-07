import random

n = int(input("Nhập số tự nhiên n: "))
A = list(range(1, n + 1))
result = []

while A:
    i = random.randint(0, len(A) - 1)
    result.append(A[i])
    A.pop(i)

print("Hoán vị ngẫu nhiên là:", result)
