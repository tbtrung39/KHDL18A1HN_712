def ucln(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
print("Ước chung lớn nhất là:", ucln(a, b))
