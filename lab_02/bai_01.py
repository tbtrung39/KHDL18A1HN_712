thang = int(input('Nhập vào 1 tháng: '))
if 1 <= thang <= 12:
    so_ngay = 31
    if thang == 2:
        so_ngay = 28
    elif thang == 4 or thang == 6\
        or thang == 9 or thang == 11:
            so_ngay = 30
    print('Tháng', thang, 'có', so_ngay, 'ngày')
else:
    print('Không có tháng', thang, 'trong năm')
    