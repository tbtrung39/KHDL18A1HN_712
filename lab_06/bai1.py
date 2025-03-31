# Danh sách cho trước
lst = [2, -4, 1, 9, -3, -6, 3, -2, 6, 8]

# 1. Tính tổng các phần tử của danh sách
tong = sum(lst)
print("Tổng các phần tử:", tong)

# 2. Đếm số lượng và tính tổng các số dương
so_duong = [x for x in lst if x > 0]
count_duong = len(so_duong)
sum_duong = sum(so_duong)
print("Số lượng số dương:", count_duong)
print("Tổng các số dương:", sum_duong)

# 3. Tìm vị trí của phần tử âm đầu tiên
vi_tri_am_dau = next((i for i, x in enumerate(lst) if x < 0), -1)
print("Vị trí phần tử âm đầu tiên:", vi_tri_am_dau)

# 4. Tìm vị trí của phần tử dương cuối cùng
vi_tri_duong_cuoi = next((i for i in range(len(lst)-1, -1, -1) if lst[i] > 0), -1)
print("Vị trí phần tử dương cuối cùng:", vi_tri_duong_cuoi)
# 5
max_val = max(lst)
vi_tri_max_cuoi = next((i for i in range(len(lst)-1, -1, -1) if lst[i] == max_val), -1)
print("Phần tử lớn nhất:", max_val)
print("Vị trí phần tử lớn nhất cuối cùng:", vi_tri_max_cuoi)
