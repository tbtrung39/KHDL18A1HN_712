from hinhhoc import my_Triangle, my_square

# Hinh vuong
print("=== Hinh vuong ===")
canh = float(input("Nhap canh hinh vuong: "))
print("Chu vi:", my_square.tinh_chu_vi(canh))
print("Dien tich:", my_square.tinh_dien_tich(canh))

# Tam giac
print("\n=== Tam giac ===")
a = float(input("Nhap canh a: "))
b = float(input("Nhap canh b: "))
c = float(input("Nhap canh c: "))

if a + b > c and a + c > b and b + c > a:
    print("Chu vi:", my_Triangle.tinh_chu_vi(a, b, c))
    print("Dien tich:", my_Triangle.tinh_dien_tich(a, b, c))
else:
    print("Ba canh khong tao thanh tam giac.")
