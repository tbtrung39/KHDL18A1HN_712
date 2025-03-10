so = int(input("Nhập một số nguyên dương: "))
while so < 0:
    print("Vui lòng nhập số nguyên dương!")
    so = int(input("Nhập một số nguyên dương: "))
so_du = so
chia = 1
while so_du >= 10:
    chia *= 10
    so_du //= 10
while chia > 0:
    print(so // chia)
    so %= chia
    chia //= 10
