from functools import reduce
danh_sach = list(range(1, 101))
so_chia_het_3 = list(filter(lambda x: x % 3 == 0, danh_sach))
tong = reduce(lambda x, y: x + y, so_chia_het_3)
print("Danh sách các số chia hết cho 3:", so_chia_het_3)
print("Tổng các số chia hết cho 3:", tong)