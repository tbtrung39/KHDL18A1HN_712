import random


characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
size_A = int(input("Nhập số phần tử cho tập hợp A: "))
size_B = int(input("Nhập số phần tử cho tập hợp B: "))

A_set = set(random.choice(characters) for _ in range(size_A))
B_set = set(random.choice(characters) for _ in range(size_B))

common_elements = A_set.intersection(B_set)

print("Tập hợp A:", A_set)
print("Tập hợp B:", B_set)
print("Các phần tử chung của A và B:", common_elements)