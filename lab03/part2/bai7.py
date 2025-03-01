n = int(input("Nhập n số nguyên đầu tiên : ")) 
tong = 0 
for i in range(1,n) : 
    tong += 1/i 
print(f"Tổng nghịch đào của {n} số nguyên đầu tiên là ",tong )
