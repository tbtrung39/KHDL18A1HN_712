def doi_thoi_gian(s, m, h, d):
    tong_giay = s + (m * 60) + (h * 3600) + (d * 86400)
    return tong_giay

s = int(input("Nhập số giây: "))
m = int(input("Nhập số phút: "))
h = int(input("Nhập số giờ: "))
d = int(input("Nhập số ngày: "))

tong = doi_thoi_gian(s, m, h, d)
print(f"Tổng số giây: {tong}")
