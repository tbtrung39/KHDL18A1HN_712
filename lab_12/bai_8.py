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
    print('Ngay truoc do:', end=' ')
    if d > 1: print(f'{d-1}-{m}-{y}')
    elif m > 1: print(f'{t[m-2]}-{m-1}-{y}')
    else: print(f'31-12-{y-1}')

except Exception as e:
    print('*', e)