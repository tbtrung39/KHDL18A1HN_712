so = int(input("Nhập số : "))
if so < 1000 : 
    hang_tram = so // 100 
    print("Số hàng trăm của số là " , hang_tram )
elif so > 1000 : 
    so = so // 100 
    hang_tram = so % 10 
    print("Số hàng trăm của số là",hang_tram )