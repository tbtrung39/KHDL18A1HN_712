# Tính cước tắc xi
loai_xe = int(input("Cho biết loại xe là 4/7 ?"))
so_km = float(input("Nhập số km chạy = "))
time_cho = float(input("Cho biết thời gian chờ (phút chờ) = "))
tien_cuoc = float(0)
tien_di_chuyen = float(0)
if time_cho >= 5:
    tien_cho = (time_cho - 5) * 800  # Chuyển 0.8 thành 800 đồng/phút
else:
    tien_cho = 0

if loai_xe == 4:
    if so_km <= 0.8:
        tien_di_chuyen = 11000
    elif so_km <= 20:
        tien_di_chuyen = 11000 + (so_km - 0.8) * 12100  # Tính tiền cho quãng đường > 0.8km
    else:
        tien_di_chuyen = 11000 + (20 - 0.8) * 12100 + (so_km - 20) * 10000  # Tính tiền cho quãng đường > 20km
    tien_cuoc = tien_cho + tien_di_chuyen
    print("Cước phí xe tacxi 4 chỗ của quý khách là %0.2f" % tien_cuoc)

elif loai_xe == 7:  # Thêm elif để xử lý trường hợp loại xe 7 chỗ
    if so_km <= 0.8:
        tien_di_chuyen = 13000
    elif so_km <= 30:
        tien_di_chuyen = 13000 + (so_km - 0.8) * 14100  # Tính tiền cho quãng đường > 0.8km
    else:
        tien_di_chuyen = 13000 + (30 - 0.8) * 14100 + (so_km - 30) * 12000  # Tính tiền cho quãng đường > 30km
    tien_cuoc = tien_cho + tien_di_chuyen
    print("Cước phí xe tacxi 7 chỗ của quý khách là %0.2f" % tien_cuoc)
else:
    print("Loại xe không hợp lệ.")  # Xử lý trường hợp nhập sai loại xe