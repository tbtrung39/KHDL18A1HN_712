ngay = int(input("Nhập só ngày : "))
gio = int(input("Nhập số giờ "))
phut = int(input("Nhập số phút "))
giay = int(input("nhập số giây "))

sogiay = (ngay * 24 * 60 * 60) + (gio * 60 * 60) + (phut *60 ) + giay 
print("số giây sau khi quy đổi", sogiay ) 