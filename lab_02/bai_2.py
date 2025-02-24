import math
print("Chương trình giải phương trình bậc hai ax^2 + bx + c = 0")
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình có vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        print("Phương trình có một nghiệm x =", -c / b)
else:
    delta = b * b - 4 * a * c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("Phương trình có hai nghiệm phân biệt x1 =", x1, "và x2 =", x2)
    elif delta == 0:
        print("Phương trình có nghiệm kép x =", -b / (2 * a))
    else:
        print("Phương trình vô nghiệm")
