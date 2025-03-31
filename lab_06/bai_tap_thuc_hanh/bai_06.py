import random


A = [random.randint(1, 99999) for _ in range(1000)]


A_sorted1 = sorted(A)
print("Danh sách đã sắp xếp (sorted()):", A_sorted1)


A_sorted2 = A[:]
n = len(A_sorted2)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if A_sorted2[j] > A_sorted2[j + 1]:
            A_sorted2[j], A_sorted2[j + 1] = A_sorted2[j + 1], A_sorted2[j]

print("Danh sách đã sắp xếp (Bubble Sort):", A_sorted2)