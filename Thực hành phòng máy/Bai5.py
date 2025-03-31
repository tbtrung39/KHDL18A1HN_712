import random
danh_sach_A = [random.randint(1, 99999) for _ in range(1000)]
print("Danh sách A ban đầu:", danh_sach_A)
danh_sach_tang = sorted(danh_sach_A)
print("\nDanh sách sắp xếp tăng dần:", danh_sach_tang)
danh_sach_giam = sorted(danh_sach_A, reverse=True)
print("\nDanh sách sắp xếp giảm dần:", danh_sach_giam)
