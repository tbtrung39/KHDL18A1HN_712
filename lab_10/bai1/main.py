import my_Triangle
a=float(input("Nhap canh a"))
b=float(input("Nhap canh b"))
c=float(input("Nhap canh c"))

if my_Triangle.is_TamGiac(a,b,c):
    print("Day la mot tam giac")
    print("Chu vi cua tam giac la: ",my_Triangle.ChuViTG(a,b,c))
    print("Dien tich tam giac la: ",my_Triangle.S_TG(a,b,c))
else:
    print("Ba canh khong tao thanh tam giac")