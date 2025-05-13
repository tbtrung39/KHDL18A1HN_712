import csv
def doc_danh_sach_sinh_vien(file_path):
    sinh_vien = {}
    with open(file_path,mode='r',encoding='utf=8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            ma_sv, ten_sv, gioi_tinh, nam_sinh = row
            sinh_vien[ma_sv] = {
                'ten_sv': ten_sv,
                'gioi_tinh': True if gioi_tinh == 'Nam' else False,
                'nam_sinh': nam_sinh
            }
    return sinh_vien
def in_danh_sach_sinh_vien(sinh_vien):
    print('Danh sach sinh vien:')
    for ma_sv, sv in sinh_vien.items():
        gioi_tinh = 'Nam' if sv['gioi_tinh'] else 'Nữ'
        print(f'{ma_sv}: {sv["ten_sv"]}, giới tính: {gioi_tinh}, năm sinh: {sv["nam_sinh"]}')
def sap_xep_sinh_vien(sinh_vien):
    sorted_sv = sorted(sinh_vien.items(), key=lambda x: x[1]['nam_sinh'], reverse=True)
    print('\nDanh sách sinh viên trước khi sắp xếp:')
    in_danh_sach_sinh_vien(sinh_vien)
    print('\nDanh sách sinh viên sau khi sắp xếp:')
    sorted_sv_dict = {k: v for k, v in sorted_sv}
    in_danh_sach_sinh_vien(sorted_sv_dict)
def them_sinh_vien(sinh_vien):
    ma_sv = input('Nhập mã sinh viên: ')
    ten_sv = input('Nhập tên sinh viên: ')
    gioi_tinh = input('Nhập giới tính (Nam/Nữ): ')
    nam_sinh = input('Nhập năm sinh: ')
    sinh_vien[ma_sv] = {
        'ten_sv': ten_sv,
        'gioi_tinh': True if gioi_tinh == 'Nam' else False,
        'nam_sinh': nam_sinh
    }
    print('\nDanh sách sinh viên sau khi thêm mới:')
    in_danh_sach_sinh_vien(sinh_vien)
def tim_kiem_sv(ma_sv, danh_sach_sv):
    if ma_sv in danh_sach_sv:
        sv = danh_sach_sv[ma_sv]
        print(f'Tên sinh viên: {sv["ten_sv"]}, giới tính: {'Nam' if sv["gioi_tinh"] else 'Nữ'}, năm sinh: {sv["nam_sinh"]}')
    else:
        print('Không tìm thấy sinh viên có mã số này.')
def xoa_sv(danh_sach_sv):
    ma_sv = input('Năm sinh của sinh viên cần xóa: ')
    for ma_sv, sv in list(danh_sach_sv.items()):
        if sv['nam_sinh'] == 'ma_sv':
            del danh_sach_sv[ma_sv]
            print('Đã xóa sinh viên có năm sinh là', ma_sv)
sinh_vien = doc_danh_sach_sinh_vien('sinhvien.csv')

sap_xep_sinh_vien(sinh_vien)

print('\nNhập thông tin sinh viên cần thêm vào:')
them_sinh_vien(sinh_vien)

print('\nNhập thông tin sinh viên cần xóa:')
xoa_sv(sinh_vien)