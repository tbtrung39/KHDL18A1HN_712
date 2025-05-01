def tim_ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))

ucln = tim_ucln(a, b)

print(f"Ước chung lớn nhất của {a} và {b} là: {ucln}")
