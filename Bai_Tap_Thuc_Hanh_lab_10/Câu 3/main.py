import sohoc

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

ucln = sohoc.Ucln(a, b)
bcnn = sohoc.Bcnn(a, b)

print(f"Ước chung lớn nhất của {a} và {b} là: {ucln}")
print(f"Bội chung nhỏ nhất của {a} và {b} là: {bcnn}")