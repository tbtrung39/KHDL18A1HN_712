import my_square

a = float(input("Nhập độ dài cạnh hình vuông: "))

chuvi = my_square.ChuViHinhVuong(a)
dientich = my_square.Dien_tich_hinh_vuong(a)

print("Chu vi hình vuông là:", chuvi)
print("Diện tích hình vuông là:", dientich)
