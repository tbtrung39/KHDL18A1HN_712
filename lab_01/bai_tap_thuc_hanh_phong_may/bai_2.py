s = int(input("Nhập số giây: "))
m = int(input("Nhập số phút: "))
h = int(input("Nhập số giờ: "))
d = int(input("Nhập số ngày: "))

tong_giay = s + m * 60 + h * 3600 + d * 86400
print(f"Tổng thời gian quy đổi là: {tong_giay} giây")
