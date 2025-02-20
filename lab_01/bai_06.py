t = float(input("Nhập thời gian sử dụng bóng đèn (giây): "))
U = 220
I = 2.7
P = U * I
t_gio = t / 3600  
A = P * t_gio / 1000  
gia_dien = 7000
tien_dien = A * gia_dien
print("Số tiền điện phải trả: %0.2f"%tien_dien,"đồng")
