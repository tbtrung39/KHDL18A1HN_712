num = int(input("Nhap so nguyen: "))
tong = 0
while num > 0:
    tong += num % 10
    num //= 10
print("Tong cac chu so la:", tong)