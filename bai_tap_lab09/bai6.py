import random

n = int(input("Nhập n: "))
A = list(range(1, n+1))
result = []

while A:
    idx = random.randint(0, len(A) - 1)
    result.append(A.pop(idx))

print("Hoán vị ngẫu nhiên:", result)
