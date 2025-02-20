print("Nhập ngày giờ phút giây")
d = int(input("Nhập số ngày: "))
h = int(input("Nhập số giờ: "))
m = int(input("Nhập số phút: "))
s = int(input("Nhập số giây: "))
m += s // 60
s = s % 60
h += m // 60
m = m % 60
d += h // 24
h = h % 24
print("Đổi giá trị : " ,d,"ngày",h,"giờ",m,"phút",s,"giây")
