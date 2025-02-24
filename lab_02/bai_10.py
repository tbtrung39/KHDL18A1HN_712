print("Chương trình tính tiền thuê sân bóng")
gbd = int(input("Nhập giờ bắt đầu: "))
gkt = int(input("Nhập giờ kết thúc: "))
if 5 <= gbd <= gkt <= 22:
    tg = gkt - gbd
    if tg <= 3:
        tien = tg * 100000
    else:
        tien = 3 * 100000 + (tg - 3) * (100000 * 0.75)
    if 11 <= gbd < 15 or 11 < gkt <= 15:
        tien *= 0.9
    print("Số tiền phải trả là %0.0f đồng" % tien)
else:
    print("Vui lòng nhập lại")