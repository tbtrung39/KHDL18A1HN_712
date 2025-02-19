d = int(input('Nhập số ngày: '))
h = int(input('Nhập số giờ: '))
m = int(input('Nhập số phút: '))
s = int(input('Nhập số giây: '))
tong_so_giay = d * 86400 + h * 3600 + m * 60 + s
print(d, 'ngày,', h, 'giờ,', m, 'phút,', s, 'giây tương ứng với', tong_so_giay, 'giây')
