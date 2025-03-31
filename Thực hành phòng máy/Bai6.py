import random
danh_sach_A = [random.randint(1, 99999) for _ in range(1000)]
print("Danh sách A ban đầu:", danh_sach_A)
for i in range(len(danh_sach_A) - 1):
    for j in range(len(danh_sach_A) - i - 1):
        if danh_sach_A[j] > danh_sach_A[j + 1]:
            danh_sach_A[j], danh_sach_A[j + 1] = danh_sach_A[j + 1], danh_sach_A[j]
print("\nDanh sách sắp xếp tăng dần:", danh_sach_A)
for i in range(len(danh_sach_A) - 1):
    for j in range(len(danh_sach_A) - i - 1):
        if danh_sach_A[j] < danh_sach_A[j + 1]:
            danh_sach_A[j], danh_sach_A[j + 1] = danh_sach_A[j + 1], danh_sach_A[j]
print("\nDanh sách sắp xếp giảm dần:", danh_sach_A)
