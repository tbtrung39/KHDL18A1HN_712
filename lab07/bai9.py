import math

n = int(input("Nhập một số tự nhiên n: "))

A = set()
B = set()

for i in range(2, n + 1):
    if all(i % j != 0 for j in range(2, int(math.sqrt(i)) + 1)):
        if n % i == 0:
            A.add(i)
        elif i < n:
            B.add(i)

print("Tập hợp A:", A)
print("Tập hợp B:", B)
