n = int(input("Nhập số n : "))
print("Các số hoàn hảo nhỏ hơn n là ")
for i in range(1,n) : 
    tong = 0 
    for j in range(1,i) : 
        if i % j == 0 : 
            tong += j 
    if tong == i and (i - j == 1) : 
        print(i)