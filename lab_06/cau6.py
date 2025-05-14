import random
A = [random.randint(1, 99999) for _ in range(1000)]
A_sorted_2 = A.copy()
n = len(A_sorted_2)

for i in range(n):
    for j in range(0, n - i - 1):
        if A_sorted_2[j] > A_sorted_2[j + 1]:
            A_sorted_2[j], A_sorted_2[j + 1] = A_sorted_2[j + 1], A_sorted_2[j]

print("10 số đầu tiên sau khi sắp xếp (sorted()):", A_sorted_2[:10])
print("10 số đầu tiên sau khi sắp xếp (Bubble Sort):", A_sorted_2[:10])