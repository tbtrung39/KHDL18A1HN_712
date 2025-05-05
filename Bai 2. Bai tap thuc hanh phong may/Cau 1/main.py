from tamgiac.my_Triangle import is_TamGiac, ChuviTamGiac, S_TamGiac

a = float(input("Nhap canh a: "))
b = float(input("Nhap canh b: "))
c = float(input("Nhap canh c: "))

if is_TamGiac(a, b, c):
    print("Day la mot tam giac.")
    print("Chu vi:", ChuviTamGiac(a, b, c))
    print("Dien tich:", S_TamGiac(a, b, c))
else:
    print("Khong phai tam giac.")
