import my_Triange

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if my_Triange.is_TamGiac(a, b, c):
    print("Đây là 1 tam giác")
    print("Chu vi:", my_Triange.ChuviTamGiac(a, b, c))
    print("Diện tích:", my_Triange.DienTichTamGiac(a, b, c))
else:
    print("Không phải là tam giác")