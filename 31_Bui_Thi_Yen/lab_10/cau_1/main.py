from my_Triangle import is_TamGiac, ChuviTamGiac, S_TamGiac

a = float(input("Nhập độ dài cạnh a: "))
b = float(input("Nhập độ dài cạnh b: "))
c = float(input("Nhập độ dài cạnh c: "))

if is_TamGiac(a, b, c):
    print(f"Ba cạnh {a}, {b}, {c} tạo thành một tam giác")
    print(f"Chu vi tam giác: {ChuviTamGiac(a, b, c)}")
    print(f"Diện tích tam giác: {S_TamGiac(a, b, c):.2f}")
else:
    print(f"Ba cạnh {a}, {b}, {c} KHÔNG tạo thành một tam giác")