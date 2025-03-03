n = int(input("Nhập n: "))
for num in range(2, n):  
    for i in range(2, int(num ** 0.5) + 1): 
        if num % i == 0:
            break 
    else:  
        print(num, end=" ")