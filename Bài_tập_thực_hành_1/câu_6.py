U = 220
I = 2.7
t = float(input("Nhập thời gian sử dụng bóng đèn(giây): "))
gia_dien=7000
P = U*I
P_kwh = (P*t)/(1000*3600)
tien_dien = P_kwh*gia_dien
print(tien_dien)
