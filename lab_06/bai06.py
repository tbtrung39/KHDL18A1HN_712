import random
A = [random.randint(1, 99999) for _ in range(1000)]
# Sắp xếp dãy bằng cách sử dụng hàm sorted()
sorted_A = sorted(A)

# Sắp xếp mà không dùng hàm sorted() 
A_copy = A.copy() 
n = len(A_copy)

for i in range(n):
    for j in range(0, n-i-1):
        if A_copy[j] > A_copy[j+1]:
            A_copy[j], A_copy[j+1] = A_copy[j+1], A_copy[j]

print("Dãy sau khi sắp xếp bằng sorted():")
print(sorted_A)

print("\nDãy sau khi sắp xếp bằng Bubble Sort:")
print(A_copy)
