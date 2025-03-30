a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]

tong = sum(a)
print("Tổng các phần tử:", tong)

so_duong = [x for x in a if x > 0]
dem_duong = len(so_duong)
tong_duong = sum(so_duong)
print("Số lượng số dương:", dem_duong)
print("Tổng các số dương:", tong_duong)

for i in range(len(a)):
    if a[i] < 0:
        print("Vị trí phần tử âm đầu tiên:", i)
        break
for i in range(len(a) - 1, -1, -1):
    if a[i] > 0:
        print("Vị trí phần tử dương cuối cùng:", i)
        break
max_val = max(a)
for i in range(len(a) - 1, -1, -1):
    if a[i] == max_val:
        print("Phần tử lớn nhất:", max_val)
        print("Vị trí phần tử lớn nhất cuối cùng:", i)
        break
