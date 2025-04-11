s = input("Nhập chuỗi nhị phân: ")
kq = 0
mu = 1
i = 0
n= 0
while True:
    if s[i:i+1] =="":
        break
    n= n+1
    i = i+1
i = n - 1
while i >=0:
    c = s[i:i+1]
    if c == '1' :
        kq = kq + mu
    elif c != '0':
        print("Chuỗi không hợp lệ!")
        exit()
    mu = mu + mu
    i = i - 1
print("Số thập phân là : ",kq)