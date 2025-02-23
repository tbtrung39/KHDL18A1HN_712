#Câu 4 :
n = int(input("Nhập vào số nguyên n:"))
if n>=100 or n<=-100 :
    so_hang_tram = (n//100)%10
    if n<0 :
        so_hang_tram = - so_hang_tram
    print(so_hang_tram)
else:
    print(0)