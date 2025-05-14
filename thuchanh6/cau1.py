a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]

tong = 0
for x in a:
    tong += x
print("Tổng các phần tử của danh sách:", tong)

dem_duong = 0
tong_duong = 0
for x in a:
    if x > 0:
        dem_duong += 1
        tong_duong += x
print("Số lượng số dương:", dem_duong)
print("Tổng các số dương:", tong_duong)

vi_tri_am_dau = -1
for i in range(len(a)):
    if a[i] < 0:
        vi_tri_am_dau = i
        break
print("Vị trí phần tử âm đầu tiên:", vi_tri_am_dau)

vi_tri_duong_cuoi = -1
for i in range(len(a)-1, -1, -1):
    if a[i] > 0:
        vi_tri_duong_cuoi = i
        break
print("Vị trí phần tử dương cuối cùng:", vi_tri_duong_cuoi)

max_val = a[0]
for x in a:
    if x > max_val:
        max_val = x

vi_tri_max_cuoi = -1
for i in range(len(a)-1, -1, -1):
    if a[i] == max_val:
        vi_tri_max_cuoi = i
        break
print("Phần tử lớn nhất:", max_val)
print("Vị trí phần tử lớn nhất cuối cùng:", vi_tri_max_cuoi)
