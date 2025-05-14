try:
    print('Nhap 3 canh a,b,c cua tam giac')
    a = input('a = ')
    b = input('b = ')
    c = input('c = ')
    assert (a.isdigit() and b.isdigit() and c.isdigit()), 'a, b, c phai la kieu so nguyen duong'
    a, b, c = int(a), int(b), int(c)
    assert a>0 and b>0 and c>0, 'a, b, c phai la kieu so nguyen duong > 0'
    assert a+b>c and a+c>b and b+c>a, 'Do dai a, b, c khong phai cua 1 tam giac'
    l = [a, b, c]
    p = (a+b+c)/2
    s = (p*(p-a)*(p-b)*(p-c))**0.5
    print('Dien tich:', round(s, 2))

except Exception as e:
    print('*', e)