a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
tong = a + b
hieu = a - b
tich = a * b

if b != 0:
    thuong = a / b
else:
    thuong = "Không thể chia cho 0"
print(f"{a} + {b} = {tong}")
print(f"{a} - {b} = {hieu}")
print(f"{a} * {b} = {tich}")
print(f"{a} / {b} = {thuong}")
