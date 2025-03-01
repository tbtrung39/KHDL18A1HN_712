import math 
n = int(input("Nhập n : "))
for i in range(2,n) : 
    check = True 
    can = int(math.sqrt(i)) 
    for j in range(2,can+1) : 
        if i % j == 0 : 
            check = False 
    if check : 
        print(i) 