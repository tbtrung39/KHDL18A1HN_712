#Câu 6: 
t = float(input("Nhập thời gian sử dụng bóng đèn: ")) 
U = 220 
I = 2.7  
P = U*I 
E = P*t / 3600 
gia_dien = 7000 
tien_dien = E * gia_dien 
result = round(tien_dien, 2) 
print(f"Tiền điện phải trả là : {result} đồng")