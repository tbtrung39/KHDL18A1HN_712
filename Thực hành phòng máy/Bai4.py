tu_so = int(input("Nhập tử số: "))
mau_so = int(input("Nhập mẫu số: "))
while mau_so == 0:
    print("Mẫu số không thể bằng 0! Vui lòng nhập lại.")
    mau_so = int(input("Nhập mẫu số: "))
print(f"Phân số vừa nhập: {tu_so}/{mau_so}")
