try:
    username = input('Nhap username: ')
    assert username.find(' ') == -1, 'Username khong duoc chua dau cach'
    assert 'a' <= username <= 'z' or\
        'A' <= username <= 'Z' or\
        '1' <= username <= '9', 'Username khong hop le'
    with open('./lab_12/bai_6.txt', 'a') as f:
        f.write(username + '@companyname.com\n')
        f.close()
except Exception as e:
    print('*', e)
