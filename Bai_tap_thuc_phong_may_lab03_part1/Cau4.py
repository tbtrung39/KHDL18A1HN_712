# Cau 44.
n = int(input("Nhap so n: "))
print("Cac so nguyen to nho hob hoac bang", n, "la:", end = " ")
for i in range(2, n+1):
    tong = 0
    for j in range(1, i+1):
        if i%j == 0:
            tong += 1
    if tong == 2:
        print(i, end = " ")