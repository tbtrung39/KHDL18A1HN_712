import sohoc

print("Chuong trinh tinh toan so hoc")

a = int(input("Nhap vao a: "))
b = int(input("Nhap vao b: "))

print("Tong cua", a, "+", b, "=", end=" ")
print(sohoc.Cong(a, b))

print("Hieu cua", a, "-", b, "=", end=" ")
print(sohoc.Tru(a, b))

print("Tich cua", a, "x", b, "=", end=" ")
print(sohoc.Nhan(a, b))

print("Thuong so", a, "/", b, "=", end=" ")
kq = sohoc.Chia(a, b)
if kq is not None:
    print(float(kq))

print("Luy thua cua", a, "mu", b, "=", end=" ")
print(sohoc.Luy_Thua(a, b))
