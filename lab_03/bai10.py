import math 
n = int(input("Nhập n : ")) 
tich = 1 
for i in range(2,n+1) : 
    check = True 
    can = int(math.sqrt(i)) 
    for j in range(2,can+1) : 
        if i % j == 0 : 
            check = False 
    if check and n % i == 0 : 
        print(i)
        tich*= i 