a = input("Nhập a : ")
b = input("Nhập b : ")
n =len(a)
m = len(b)
tim_thay = False
for i in range(1<<(n - 1)):
    expr1 = ''
    tong1 = 0
    so = a[0]
    for j in range(1,n):
        if (i >>(j - 1)) & 1:
            tong1 += int(so)
            expr1 += so + "+"
            so = a[j]
        else:
            so += a[j]
    tong1 += int(so)
    expr1 +=so
    for k in range(1 << (m -1)):
        expr2 = ''
        tong2 = 0
        so2 = b[0]
        for l in range(1,m):
            if (k >> (l-1))& 1:
                tong2 += int(so2)
                expr2 += so2 + "+"
                so2 = b[l]
            else:
                so2 += b[l]
        tong2 += int(so2)
        expr2 += so2
    
        if tong1 == tong2 :
            print(expr1 + '=' + expr2)
            tim_thay = True
            break
    if tim_thay:
        break
if not tim_thay:
    print('Không tồn tại cách đặt!')
