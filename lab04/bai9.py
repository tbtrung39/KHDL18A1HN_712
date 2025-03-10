n = int(input("Nhập số bất kì : ")) 
tong = 0 
while True : 
    tong+= n%10 
    if n // 10 == 0 : 
        break 
    n = int(n//10) 
print(f"Tổng các chữ số của số {n} là {tong}") 