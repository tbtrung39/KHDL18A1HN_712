t1 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

try:
    d, m, y = input('Nhap 1 ngay (dd-mm-yyyy): ').split('-')
    assert (d+m+y).isdigit(), 'Ngay, thang, nam phai la so nguyen'
    d, m, y = int(d), int(m), int(y)
    assert y > 0, 'Nam phai la so nguyen duong > 0'
    assert 0 < m < 13, f'Khong co thang {m} trong nam'
    t = t1 if y%4 == 0 and y%100 != 0 else t2
    assert 0 < d <= t[m-1], f'Khong co ngay {d} trong thang'
    print(f'Ngay nay thuoc tuan', 365//7-1 if 365%7 else (365-365%7)//7,'trong nam')

except Exception as e:
    print('*', e)