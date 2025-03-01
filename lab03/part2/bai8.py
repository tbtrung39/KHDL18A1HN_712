n = int(input("Nhập n : "))
ketqua1 = 0 
if n <= 0 : 
    print("Nhập sai vui lòng nhập lại ")
else :
 #a
 for i in range(0,n+1) :
    ketqua1 += i 
 print("kết quả của a = ",ketqua1 )
 #b
 ketqua2 = 0 
 for j in range(n+1) :
    ketqua2 += (2*j) + 1 
 print("Kết quả của b =  ",ketqua2)
 #c 
 ketqua3 = 0 
 for k in range(n+1) : 
    ketqua3 += 2*k 
 print("Kết quả của c = ", ketqua3 )



