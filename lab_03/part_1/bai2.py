n = int(input("Nhập n: "))
print("Các số hoàn hảo nhỏ hơn", n, "là:", end=" ")
for so in range(1, n):  
    tong_uoc = 0  
    for i in range(1, so):  
        if so % i == 0:  
            tong_uoc += i  
    if tong_uoc == so:  
        print(so, end=" ") 