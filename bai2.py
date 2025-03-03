n = int(input("Nhập n: "))
print("Các số hoàn hảo nhỏ hơn",n,'là:')
for num in range(1, n):
    tong_uoc = 0     
    for i in range(1, num):
        if num % i == 0:
            tong_uoc += i    
    if tong_uoc == num:
        print(num)
