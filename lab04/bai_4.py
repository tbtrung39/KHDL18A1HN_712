tu_so = int(input("Nhập tử số: "))
mau_so = int(input("Nhập mẫu số: "))
while mau_so == 0:
    print("Mẫu số không được bằng 0. Vui lòng nhập lại.")
    mau_so = int(input("Nhập mẫu số: "))
print("Phân số vừa nhập là:", tu_so, "/", mau_so)