t = float(input("Nhập thời gian sử dụng bóng đèn (giây): "))
U = 220
I = 2.7
gia_dien = 7000
P = U * I
E = P * t
E_kWh = E/(1000*3600)
tien_dien = E_kWh * gia_dien
print(f"Tiền điện phải trả là: {tien_dien} đồng")