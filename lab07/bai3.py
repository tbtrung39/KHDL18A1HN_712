import random

n = int(input("Nhập số lượng phần tử: "))

A = set()

while len(A) < n:
    x = random.uniform(0, 100)  

print("Tập hợp A:", A)

print("Phần tử nhỏ nhất:", min(A))
print("Phần tử lớn nhất:", max(A))
print("Tổng các phần tử:", sum(A))
