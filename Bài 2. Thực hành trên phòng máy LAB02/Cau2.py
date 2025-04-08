# Cau2.
import math
def giai_pt_bac_hai(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "Phương trình có vô số nghiệm"
            else:
                return "Phương trình vô nghiệm"
        else:
            return f"Phương trình có một nghiệm: {-c / b}"
    else:
        delta = b**2 - 4*a*c
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            return f"Phương trình có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}"
        elif delta == 0:
            x = -b / (2*a)
            return f"Phương trình có nghiệm kép: x = {x}"
        else:
            return "Phương trình vô nghiệm"
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
ket_qua = giai_pt_bac_hai(a, b, c)
print(ket_qua)