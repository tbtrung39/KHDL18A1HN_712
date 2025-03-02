#Câu 3 :
n=int(input("Nhập số nguyên n:"))
if n<=1:
    print(n,"không là số nguyên tố và số nguyên tố gần nhất là 2")
else:
    for i in range(2,int(n**0.5)+1):
        if n%i==0  :
            so_tren=n+1
            so_duoi=n-1
            for j in range(so_tren,so_tren+100):
                for k in range(2,int(j**0.5)+1):
                    if j%k==0:
                        break
                    else:
                        so_tren = j
                        break
            for t in range(so_duoi,so_duoi-100,-1):
                if t <=1:
                    break
                for r in range(2,int(t**0.5)+1):
                    if t%r==0:
                        break
                else:
                    so_duoi = t
                    break   
            if so_tren-n <= n-so_duoi:
                print(n,"không là số nguyên tố và số nguyên tố gần nhất là:",so_tren)
            else:
                print(n,"không là số nguyên tố và số nguyên tố gần nhất là:",so_duoi) 
                break              
    else: 
        print(n,"là số nguyên tố")
