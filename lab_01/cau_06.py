t = float(input("Nhập thời gian sử dụng bóng đèn (giây): ")) 
U = 220 
I = 2.7   
gia_tien = 7000 
P = U * I 
so_dien = (P * t) / (1000 * 3600)
tien_dien = so_dien * gia_tien 
print(f"Tiền điện phải trả là: {tien_dien} đ") 
