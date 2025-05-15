# Câu 6
import random
#
A = [random.randint(1, 999999) for _ in range(1000)]
A_sorted = sorted(A)
print("Danh sach sau khi sap xep bang sorted():", A_sorted)
print()
#
def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst
A_selection_sorted = selection_sort(A.copy())
print("Danh sach sau khi sap xep bang Selection Sort:", A_selection_sorted)