# Câu 11.	Tìm hai số nguyên tố liên tiếp có khoảng cách xa nhất trong khoảng từ 1 đến N.

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
N = int(input("Nhập số nguyên dương N: "))
ds_nguyen_to = []
for i in range(2, N + 1):
    if la_so_nguyen_to(i):
        ds_nguyen_to.append(i)
khoang_cach_max = 0
so_1 = so_2 = 0
for i in range(len(ds_nguyen_to) - 1):
    khoang_cach = ds_nguyen_to[i + 1] - ds_nguyen_to[i]
    if khoang_cach > khoang_cach_max:
        khoang_cach_max = khoang_cach
        so_1 = ds_nguyen_to[i]
        so_2 = ds_nguyen_to[i + 1]

if khoang_cach_max == 0:
    print("Không có hai số liên tiếp trong khoảng từ 1 đến ", N)
else:
    print("Hai số nguyên tô liên tiếp có khoảng cách xa nhất là: ", so_1, "và", so_2)
    print("Khoảng cách là :", khoang_cach_max)
