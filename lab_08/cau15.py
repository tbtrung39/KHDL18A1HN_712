n = int(input("Nhập số lượng phần tử n: "))
lst = []

for i in range(n):
    so = int(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(so)

so_le = list(filter(lambda x: x % 2 != 0, lst))

binh_phuong_le = list(map(lambda x: x**2, so_le))

print("List gốc:", lst)
print("List số lẻ:", so_le)
print("List bình phương số lẻ:", binh_phuong_le)
