import random

# Tạo danh sách 1000 số ngẫu nhiên
danh_sach = [random.randint(1, 99999) for _ in range(1000)]

# 1. Sắp xếp dùng hàm sorted
sap_xep_co_san = sorted(danh_sach)
print("1000 số đầu (dùng sorted):", sap_xep_co_san[:1000])

# 2. Sắp xếp không dùng sorted (thuật toán chọn)
def sap_xep_chon(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

danh_sach_sx = danh_sach.copy()
sap_xep_chon(danh_sach_sx)
print("1000 số đầu (tự sắp xếp):", danh_sach_sx[:1000])