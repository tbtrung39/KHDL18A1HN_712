U = 220 
I = 2.7 
Gia_dien = 7000 
t = float(input("Nhập thời gian sử dụng bóng đèn (giây): "))
P = U * I  
E = (P * t) / 3600
Tien_dien = (E / 1000) * Gia_dien 
print("Tiền điện phải trả là:", round(Tien_dien, 2), "đ")
