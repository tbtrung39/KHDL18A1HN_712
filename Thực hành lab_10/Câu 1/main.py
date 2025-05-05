import my_Triangle

a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

if my_Triangle.is_TamGiac(a, b, c):
    print("Đây là tam giác hợp lệ.")
    chu_vi = my_Triangle.ChuviTamGiac(a, b, c)
    dien_tich = my_Triangle.S_TamGiac(a, b, c)
    print(f"Chu vi tam giác: {chu_vi}")
    print(f"Diện tích tam giác: {dien_tich}")
else:
    print("Ba cạnh không tạo thành một tam giác.")