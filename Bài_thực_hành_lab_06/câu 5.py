import random
lst = [random.randint(1, 99999) for _ in range (1000)]
sorted_lst1 = sorted(lst)
print("Sắp xếp bằng sorted(): ", sorted_lst1)