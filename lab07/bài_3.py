import random

n = int(input("Nhập số phần tử: "))
A = {random.uniform(0, 100) for _ in range(n)}  

print("Tập hợp A:", A)
print("Min:", min(A))
print("Max:", max(A))
print("Tổng:", sum(A))