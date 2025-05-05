from hinhhoc import my_square,my_Triangle
a=float(input("Nhap do dai canh hinh vuong"))
print("Chu vi HV la: ",my_square.ChuviHV(a))
print("Dien tich HV la: ",my_square.S_HV(a))

a1=float(input("Nhap canh a"))
b=float(input("Nhap canh b"))
c=float(input("Nhap canh c"))

if my_Triangle.is_TamGiac(a1,b,c):
    print("Day la mot tam giac")
    print("Chu vi cua tam giac la: ",my_Triangle.ChuViTG(a1,b,c))
    print("Dien tich tam giac la: ",my_Triangle.S_TG(a1,b,c))
else:
    print("Ba canh khong tao thanh tam giac")
