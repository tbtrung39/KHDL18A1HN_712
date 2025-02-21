import math

def solve_quadratic(a, b, c):
    if a == 0:
        if b == 0:
            return "Phương trình vô nghiệm" if c != 0 else "Phương trình có vô số nghiệm"
        return f"Phương trình có nghiệm duy nhất: x = {-c / b}"

    delta = b**2 - 4*a*c
    if delta < 0:
        return "Phương trình vô nghiệm"
    elif delta == 0:
        return f"Phương trình có nghiệm kép: x = {-b / (2*a)}"
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"Phương trình có hai nghiệm: x1 = {x1}, x2 = {x2}"

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
print(solve_quadratic(a, b, c))