import random

n = int(input())
A = list(range(1, n + 1))
result = []

while A:
    chosen = random.choice(A)
    result.append(chosen)
    A.remove(chosen)

print(result)
