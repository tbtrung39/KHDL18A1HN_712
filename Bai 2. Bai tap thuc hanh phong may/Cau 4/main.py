import giaiphuongtrinh

print("Giai phuong trinh bac nhat: ax + b = 0")
a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
print(giaiphuongtrinh.giai_pt_bac_nhat(a, b))

print("\nGiai phuong trinh bac hai: ax^2 + bx + c = 0")
a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))
print(giaiphuongtrinh.giai_pt_bac_hai(a, b, c))
