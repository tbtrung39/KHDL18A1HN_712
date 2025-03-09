n = int(input("Nhap so nguyen: "))
tong = 0
while n!= 0:
    tong += n % 10
    n //= 10
print("Tong hai chu so cua so vua nhap la: ", tong)