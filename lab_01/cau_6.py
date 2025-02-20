#Bài 6
s=int(input("nhập thời gian sử dụng bóng đèn (giây) là: "))
u = 220
i = 2.7
gia_tien=7000
p=u*i
e=p*s/3600000
tien_dien=e*gia_tien
print("giá tiền diện phải trả là:",tien_dien)