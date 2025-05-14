n = int(input("Nhập số lượng phần tử n: "))
lst = []

for i in range(n):
    so = int(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(so)

lst_binh_phuong = list(map(lambda x: x**2, lst))

print("List gốc:", lst)
print("List bình phương:", lst_binh_phuong)
