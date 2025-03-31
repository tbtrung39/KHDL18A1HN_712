import random

# Sinh danh sách A gồm 1000 số tự nhiên ngẫu nhiên trong khoảng [1, 99999]
A = [random.randint(1, 99999) for _ in range(1000)]

# Cách 1: Sử dụng hàm sorted()
sorted_A1 = sorted(A)
print("Danh sách sắp xếp tăng dần (cách 1 - dùng sorted()):", sorted_A1[:10], "...")

# Cách 2: Sắp xếp thủ công (thuật toán sắp xếp nổi bọt - Bubble Sort)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

sorted_A2 = A[:]  
bubble_sort(sorted_A2)
print("Danh sách sắp xếp tăng dần (cách 2 - không dùng sorted()):", sorted_A2[:10], "...")
