num = int(input("Nhập một số nguyên: "))
tong = 0
so = abs(num) 
while so > 0:
    tong += so % 10
    so //= 10
print("Tổng các chữ số của số vừa nhập là:", tong)
