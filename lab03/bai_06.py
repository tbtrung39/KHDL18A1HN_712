n = int(input("Nhập số n: "))
tong_bac_3 = 0
for i in range(1, n + 1):
    tong_bac_3 += i ** 3
print(f"Tổng bậc 3 của {n} số nguyên dầu tiên là: {tong_bac_3}")