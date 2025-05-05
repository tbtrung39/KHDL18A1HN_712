import phuongtrinh

print("Giải phương trình bậc nhất: ax + b = 0")
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
print(phuongtrinh.giai_pt_bac_nhat(a, b))

print("Giải phương trình bậc hai: ax^2 + bx + c = 0")
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
print(phuongtrinh.giai_pt_bac_hai(a, b, c))