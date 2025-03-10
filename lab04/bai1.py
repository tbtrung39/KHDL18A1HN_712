n = int(input("Nhập n : ")) 
if n <= 0 : 
    print("NHập sai yêu cầu nhập lại ") 
else : 
    tonga = 0 
    soa = 0 
    while soa <=  n : 
        tonga += soa**2 
        soa += 1 
    tongb = 0 
    sob = 0 
    while sob <= n : 
        tongb = (2*sob +1)**3 
        sob += 1 
    tongc = 0 
    soc = 0 
    while soc <= n : 
        tongc = (2*soc)**4 
        soc += 1 
    print("Tổng của câu a là = ",tonga )
    print("Tổng của câu b là = ",tongb )
    print("Tổng của câu c là = ",tongc )