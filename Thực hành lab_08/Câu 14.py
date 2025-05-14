#Câu 14:
n = int(input("Nhập số phần tử của list: "))
lst = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(x)
binh_phuong = list(map(lambda x: x**2, lst))
print("List các bình phương:", binh_phuong)