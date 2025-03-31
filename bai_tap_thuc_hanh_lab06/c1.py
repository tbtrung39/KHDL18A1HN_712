# Danh sách đã cho
lst = [-2, 4, 1, 9, 3, 6, 3, -2, 6, 8]

# 1. Tính tổng các phần tử trong danh sách
tong = 0
for x in lst:
    tong += x
print("Tổng các phần tử:", tong)

# 2. Đếm số lượng số dương và tính tổng của chúng
dem_duong = 0
tong_duong = 0
for x in lst:
    if x > 0:
        dem_duong += 1
        tong_duong += x
print("Số lượng số dương:", dem_duong)
print("Tổng các số dương:", tong_duong)

# 3. Tìm vị trí phần tử âm đầu tiên
vi_tri_am_dau = -1
for i in range(len(lst)):
    if lst[i] < 0:
        vi_tri_am_dau = i
        break
print("Vị trí phần tử âm đầu tiên:", vi_tri_am_dau)

# 4. Tìm vị trí phần tử dương cuối cùng
vi_tri_duong_cuoi = -1
for i in range(len(lst) - 1, -1, -1):
    if lst[i] > 0:
        vi_tri_duong_cuoi = i
        break
print("Vị trí phần tử dương cuối cùng:", vi_tri_duong_cuoi)

# 5. Tìm phần tử lớn nhất và vị trí của nó
max_value = lst[0]
vi_tri_max = 0
for i in range(1, len(lst)):
    if lst[i] > max_value:
        max_value = lst[i]
        vi_tri_max = i
print("Phần tử lớn nhất:", max_value)
print("Vị trí phần tử lớn nhất:", vi_tri_max)

# 6. Tìm phần tử nhỏ nhất cuối cùng
min_value = lst[0]
vi_tri_min_cuoi = 0
for i in range(len(lst)):
    if lst[i] <= min_value:
        min_value = lst[i]
        vi_tri_min_cuoi = i
print("Phần tử nhỏ nhất cuối cùng:", min_value)
print("Vị trí phần tử nhỏ nhất cuối cùng:", vi_tri_min_cuoi)