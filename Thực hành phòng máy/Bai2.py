s = int(input("Nhập số giây: "))
m = int(input("Nhập số phút: "))
h = int(input("Nhập số giờ: "))
d = int(input("Nhập số ngày: "))
tong_giay = d*24*60*60 + h*60*60 + m*60 + s
print("Tổng số giây: ",tong_giay)
