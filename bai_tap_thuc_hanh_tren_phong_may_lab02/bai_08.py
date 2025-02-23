luongcoban=1350000
tham_nien=int(input('Nhập thâm niên: '))
if tham_nien<12:
    he_so=2.34
    luong_thuc_te=he_so*luongcoban
    print('Lương là: ',luong_thuc_te)
elif 12<=tham_nien<36:
    he_so=3.33
    luong_thuc_te=he_so*luongcoban
    print('Lương là: ',luong_thuc_te)
elif 36<=tham_nien<60:
    he_so=3.66
    luong_thuc_te=he_so*luongcoban
    print('Lương là: ',luong_thuc_te)
elif 60<tham_nien:
    he_so=3.99
    luong_thuc_te=he_so*luongcoban
    print('Lương là: ',luong_thuc_te)
else:
    print('Thâm niên không hợp lệ, vui lòng nhập lại')
    