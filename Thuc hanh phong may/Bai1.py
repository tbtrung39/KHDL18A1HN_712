import my_Triangle

a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

if my_Triangle.is_TamGiac(a, b, c):
    print("Ba cạnh tạo thành tam giác.")
    print("Chu vi tam giác:", my_Triangle.ChuViTamGiac(a, b, c))
    print("Diện tích tam giác:", my_Triangle.S_TamGiac(a, b, c))
else:
    print("Ba cạnh KHÔNG tạo thành tam giác.")
