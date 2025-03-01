n = int(input("Nhập n số nguyên đầu tiên : "))
tong = 0 
for i in range(1,n+1) :
    tong += i**3 
print(f"Tổng bậc 33 của {n} số nguyên đầu tiên là",tong)  
