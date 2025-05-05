import my_square

a = float(input("Nhập độ dài cạnh hình vuông: "))

chu_vi = my_square.ChuviHinhvuong(a)
dien_tich = my_square.Dien_tich_hinh_vuong(a)

if chu_vi is not None and dien_tich is not None:
    print(f"Chu vi hình vuông: {chu_vi}")
    print(f"Diện tích hình vuông: {dien_tich}")
else:
    print("Độ dài cạnh không hợp lệ. Vui lòng nhập số lớn hơn 0.")