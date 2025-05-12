from sohoc import Ucln, Bcnn, SumDivisors

# Chương trình chính
print("1. Tính UCLN và BCNN của 2 số")
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
print(f"Ước chung lớn nhất của {a} và {b} là: {Ucln(a, b)}")
print(f"Bội chung nhỏ nhất của {a} và {b} là: {Bcnn(a, b)}")

print("\n2. Tính tổng các ước số của một số")
n = int(input("Nhập số nguyên dương: "))
print(f"Tổng các ước số của {n} (không bao gồm chính nó) là: {SumDivisors(n)}")