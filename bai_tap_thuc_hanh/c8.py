import random

integers = [random.randint(1, 100) for _ in range(5)]
floats = [random.uniform(1, 100) for _ in range(5)]  
strings = [''.join([random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(3)]) for _ in range(5)]  

A = set(integers + floats + strings)


count_integers = 0
count_floats = 0
count_strings = 0

for item in A:
    if isinstance(item, int):
        count_integers += 1
    elif isinstance(item, float):
        count_floats += 1
    elif isinstance(item, str):
        count_strings += 1

print("Tập hợp A:", A)
print("Số phần tử là số nguyên:", count_integers)
print("Số phần tử là số thực:", count_floats)
print("Số phần tử là chuỗi ký tự:", count_strings)