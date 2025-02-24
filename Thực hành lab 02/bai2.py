import math
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
if a == 0:
    if b == 0:
        print("Phương trình vô nghiệm" if c != 0 else "Phương trình có vô số nghiệm")
    else:
        x = -c / b
        print(f"Phương trình có một nghiệm: x = {x}")
else:
    # Tính delta
    delta = b**2 - 4*a*c    
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Phương trình có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Phương trình có nghiệm kép: x = {x}")
    else:
        print("Phương trình vô nghiệm")
