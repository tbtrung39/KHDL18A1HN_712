from sohoc import Ucln, Bcnn, SumDivisor

a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))
n = int(input("Nhap so nguyen n: "))

print("Uoc chung lon nhat la: ", Ucln(a, b))
print("Boi chung nho nhat la: ", Bcnn(a, b))
print(f"Tong cac uoc cua {n} la: ", SumDivisor(n))
