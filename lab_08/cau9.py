def cong(a, b):
    return a + b

def tru(a, b):
    return a - b

def nhan(a, b):
    return a * b

def chia(a, b):
    if b == 0:
        return "Không thể chia cho 0!"
    return a / b

a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))

print(f"{a} + {b} = {cong(a, b)}")
print(f"{a} - {b} = {tru(a, b)}")
print(f"{a} * {b} = {nhan(a, b)}")
print(f"{a} / {b} = {chia(a, b)}")
