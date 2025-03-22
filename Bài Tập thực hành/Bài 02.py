s = int(input("Nhập số giây: "))
m = int(input("Nhập số phút: "))
h = int(input("Nhập số giờ: "))
d = int(input("Nhập số ngày: "))

# Tính tổng số giây
tong_giay = d * 86400 + h * 3600 + m * 60 + s

# Tính số ngày, giờ, phút, giây
ngay = tong_giay // 86400
gio = (tong_giay % 86400) // 3600
phut = (tong_giay % 3600) // 60
giay = tong_giay % 60

# In kết quả
print(f"{ngay} ngày, {gio} giờ, {phut} phút, {giay} giây")