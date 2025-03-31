
a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
tong = sum(a)
print(f"Tổng các phần tử trong danh sách là: {tong}")
so_luong_duong = sum(1 for x in a if x > 0)
tong_duong = sum(x for x in a if x > 0)
print(f"Số lượng các số dương: {so_luong_duong}, Tổng các số dương: {tong_duong}")

vitria_am = next((i for i, x in enumerate(a) if x < 0), None)
if vitria_am is not None:
    print(f"Vị trí của phần tử âm đầu tiên là: {vitria_am}")
else:
    print("Không có phần tử âm trong danh sách.")
vitriduong_cuoi = next((i for i in range(len(a)-1, -1, -1) if a[i] > 0), None)
if vitriduong_cuoi is not None:
    print(f"Vị trí của phần tử dương cuối cùng là: {vitriduong_cuoi}")
else:
    print("Không có phần tử dương trong danh sách.")
max_value = max(a)
vitrimax_cuoi = len(a) - 1 - a[::-1].index(max_value)
print(f"Phần tử lớn nhất là: {max_value}, Vị trí của phần tử lớn nhất cuối cùng là: {vitrimax_cuoi}")
