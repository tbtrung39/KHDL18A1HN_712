n = int(input("Nhập n "))
if n <= 0 : 
    print("Nhập sai vui lòng nhập lại")
else : 
    #a 
    tonga = 0 
    for i in range(1,n+1) : 
        tonga += i**2 
    #b
    tongb = 0 
    for j in range(1,n+1,2) : 
        tongb += i**3 
    #c 
    tongc = 0 
    for c in range(1,n+1) : 
        tongc += (2*n)**4 
    print("Tổng a = ",tonga )
    print("Tổng b = ",tongb )
    print("Tổng c = ",tongc )