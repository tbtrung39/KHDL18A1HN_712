U = 220
I = 2.7 
gia_dien = 7000
t = float(input("Nhập thời gian sử dụng bóng đèn (giây): "))
P = U * I 
E = P * (t / 3600) / 1000 
tien_dien = E * gia_dien 
print("Tiền điện phải trả là: %0.2f VND" % tien_dien)
