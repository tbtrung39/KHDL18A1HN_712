import math
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
if a == 0:
    if b == 0:
        print("Phương trình vô nghiệm")
    else:
        print(f"Nghiệm x = {-c / b}")
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        print(f"Phương trình có nghiệm kép x = {-b / (2*a)}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Nghiệm x1 = {x1}, x2 = {x2}")
