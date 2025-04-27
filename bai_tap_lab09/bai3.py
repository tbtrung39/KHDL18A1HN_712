def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)

a = int(input("Nhập cơ số a: "))
b = int(input("Nhập số mũ b: "))

print(f"{a}^{b} =", power(a, b))
