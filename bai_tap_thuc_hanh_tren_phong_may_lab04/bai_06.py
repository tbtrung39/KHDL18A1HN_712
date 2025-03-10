n = int(input("Nhập một số nguyên dương: "))
while n < 0:
    print("Vui lòng nhập số nguyên dương!")
    n = int(input("Nhập một số nguyên dương: "))
so_du = n
chia = 1
while so_du >= 10:
    chia *= 10
    so_du //= 10
while chia > 0:
    print(n//chia)
    n%=chia
    chia//= 10