# Cau 15.

n = int(input("Nhập số phần tử của list: "))
lst = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(x)
so_le = list(filter(lambda x: x % 2 != 0, lst))
binh_phuong_le = list(map(lambda x: x**2, so_le))
print("Danh sách các số lẻ:", so_le)
print("Bình phương các số lẻ:", binh_phuong_le)
