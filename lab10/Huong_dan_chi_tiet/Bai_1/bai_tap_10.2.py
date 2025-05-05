import sohoc
print("Chuong trinh tinh toan so hoc")
a=int(input("Nhap vao a: "))
b=int(input("Nhap vao b: "))

print(f"Tong cua {a} + {b} = ",end=" ")
print(sohoc.Cong(a,b))

print(f"Hieu cua {a} - {b} = ",end=" ")
print(sohoc.Tru(a,b))

print(f"Tich cua {a} * {b} = ",end=" ")
print(sohoc.Nhan(a,b))

print(f"Thuong so cua {a} / {b} = ",end=" ")
print(float(sohoc.Chia(a,b)))

print(f"Luy thua cua {a} mu {b} = ",end=" ")
print(sohoc.Luy_Thua(a,b))

