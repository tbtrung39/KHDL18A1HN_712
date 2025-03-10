n= int(input("Nhập n: "))
tong_lap_phuong = 0
for i in range(1, n + 1):
    tong_lap_phuong += i ** 3 
print(f"Tổng lũy thừa bậc 3 của {n} số nguyên đầu tiên là: {tong_lap_phuong}")