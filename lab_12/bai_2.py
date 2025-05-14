try:
    s = input('Nhap 1 chuoi ky tu: ')
    assert s.isalpha(), 'Loi ky tu !!!'
    for i in range(len(s)-1):
        if len(s) > 4 and s[i] == s[i+1] == s[i+2] == s[i+3] == s[i+4]:
            raise Exception('Loi nhap trung lap !!!')
        elif len(s) > 3 and s[i] == s[i+1] == s[i+2] == s[i+3]:
            raise Exception('Loi nhap lap lai !!!')
        elif len(s) > 1 and s[i] == s[i+1]:
            raise Exception('Loi nhap lieu !!!')

except Exception as e:
    print('*', e)