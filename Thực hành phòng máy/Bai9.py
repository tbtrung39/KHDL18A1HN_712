so = int(input("Nhập một số nguyên dương: "))
while so <= 0:
    print("Vui lòng nhập số nguyên dương!")
    so = int(input("Nhập một số nguyên dương: "))
tong = 0
while so > 0:
    tong += so % 10
    so //= 10
print("Tổng các chữ số là:", tong)
