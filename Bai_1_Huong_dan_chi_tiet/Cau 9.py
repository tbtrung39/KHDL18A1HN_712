# Cau 9. Dvq
import csv

def doc_danh_sach_sinh_vien(file_path):
    sinh_vien = {}
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            ma_sv,ten_sv,gioi_tinh,nam_sinh = row
            sinh_vien[ma_sv]={
                'ten_sv':ten_sv,
                'gioi_tinh':True if gioi_tinh =="Nam" else False,
                'nam_sinh': nam_sinh
            }
    return sinh_vien

def in_danh_sach_sinh_vien(sinh_vien):
    print('Danh sach sinh vien:')
    for ma_sv,sv in sinh_vien.items():
        gioi_tinh = 'Nam' if sv['gioi_tinh'] else 'Nu'     
        print(f'{ma_sv}: {sv["ten_sv"]}, gioi tinh: {gioi_tinh}, nam sinh: {sv["nam_sinh"]}')

def sap_xep_sinh_vien(sinh_vien):
    sorted_sv = sorted(sinh_vien.items(), key=lambda  x:x[1]['nam_sinh'],reverse=True)
    print('\nDanh sach sinh vien truoc khi sap xep:')
    in_danh_sach_sinh_vien(sinh_vien)
    print('\nDanh sach sinh vien sau khi sap xep:')
    sorted_sv_dict={k:v for k,v in sorted_sv}
    in_danh_sach_sinh_vien(sorted_sv_dict)

def them_sinh_vien(sinh_vien):
    ma_sv=input('Nhap ma sinh vien: ')
    ten_sv=input("Nhap ten sinh vien: ")
    gioi_tinh=input("Nhap gioi tinhs(nam/nu): ")
    nam_sinh=input("Nhap nam sinh: ")
    sinh_vien[ma_sv]={
        'ten_sv':ten_sv,
        'gioi_tinh':True if gioi_tinh =='Nam' else False,
        'nam_sinh':nam_sinh
    }
    print('\nDanh sach sinh vien sau khi them moi: ')
    in_danh_sach_sinh_vien(sinh_vien)

def tim_kien_sv(ma_sv,danh_sach_sv):
    if ma_sv in danh_sach_sv:
        sv=danh_sach_sv[ma_sv]
        print(f'Ten sinh vien:{sv["ten_sv"]},gioi tinh: {"Nam" if sv["gioi_tinh"] else "Nu"},nam sinh: {sv["nam_sinh"]}')
    else:
        print('Khong tim thay sinh vien co ma so nay.')

def xoa_sv(danh_sach_sv):
    ma_sv = int(input('Ma sinh vien can xoa: '))
    for ma_sv,sv in list(danh_sach_sv.items()):
        if sv['nam_sinh']=='ma_sv':
            del danh_sach_sv[ma_sv]
    print('Da xoa sinh vien co nam sinh la',ma_sv)

sinh_vien = doc_danh_sach_sinh_vien('Bai_1_Huong_dan_chi_tiet\sinhvien.csv')
sap_xep_sinh_vien(sinh_vien)
print('Nhap thong tin sinh vien can them vao:')
them_sinh_vien(sinh_vien)
print('Nhap thong tin sinh vien can xoa:')
xoa_sv(sinh_vien)
