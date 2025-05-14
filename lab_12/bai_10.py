from datetime import date

t1 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

try:
    d1, m1, y1 = input('Nhap ngay thu nhat (dd-mm-yyyy): ').split('-')
    d2, m2, y2 = input('Nhap ngay thu hai (dd-mm-yyyy): ').split('-')
    assert (d1+m1+y1+d2+m2+y2).isdigit(), 'Ngay, thang, nam phai la so nguyen'
    d1, m1, y1 = int(d1), int(m1), int(y1)
    d2, m2, y2 = int(d2), int(m2), int(y2)
    d1 = date(y1, m1, d1)
    d2 = date(y2, m2, d2)

    print('2 ngay cach nhau', (d2 - d1).days, 'ngay')

except ValueError as e:
    print('* Nhap ngay, thang, nam khong dung')