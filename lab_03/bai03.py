n = int(input("Nhập n : "))
 
can = int(n**0.5) 
check = True 
for i in range(2,can+1) : 
    if n % i == 0 :
        check = False  
        
if check : 
    print(f"Số {n} là số nguyên tố")
else: 
    for k in range(2,n) : 
        can2 = int(k**0.5) 
        check2 = True
        for o in range(2,can2+1 ) : 
            if k % o == 0 : 
                check = False 
    if check2 : 
            print(f"Số nguyên tố gần {n} nhất là {k}")