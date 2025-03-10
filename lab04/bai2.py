n = int(input("Nhập số n : ")) 
if n <= 0 : 
    print("Nhập sai vui lòng nhập lại : ") 
else : 
    tonga = 0 
    soa = 1 
    while soa <= n : 
        if soa % 2 == 0: 
            tonga += 1/(-soa) 
        elif soa % 2 != 0 : 
            tonga += 1/(soa) 
        soa += 1 
    tongb = 0  
    sob = 1
    while sob <= n : 
        tongb += 1/(sob*(sob+1))
        sob += 1 
    tongc = 0 
    soc = 2 
    while soc <= n :
        tongc+= 1/(soc**(1/2))
        soc += 1 
    print("Tổng của câu a là = ",tonga ) 
    print("Tổng của câu b là = ",tongb )
    print("Tổng của câu c là = ",tongc )
