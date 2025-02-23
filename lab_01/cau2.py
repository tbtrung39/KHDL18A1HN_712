seconds = int(input("Nhập số giây: "))
d = seconds // (24 * 3600)
seconds = seconds % (24 * 3600)
h = seconds // 3600
seconds = seconds % 3600
m = seconds // 60
s = seconds % 60
print(d, "ngày,", h, "giờ,", m, "phút,", s, "giây")