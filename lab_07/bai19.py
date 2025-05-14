#a
nhan_vien = {}
#b
n = int(input('Nhập số lượng nhân viên: '))
for _ in range(n):
    ma_nhan_vien = input('Nhập mã nhân viên (4 ký tự số): ')
    ho_ten = input('Nhập họ tên nhân viên (tối đa 20 ký tự): ')
    nam_sinh = int(input('Nhập năm sinh: '))
    luong = float(input('Nhập lương: '))
    nhan_vien[ma_nhan_vien] = {
        'ho_ten': ho_ten,
        'nam_sinh': nam_sinh,
        'luong': luong
    }
#c
ma_tim_kiem = input('Nhập mã nhân viên để tìm kiếm: ')
if ma_tim_kiem in nhan_vien:
    thong_tin = nhan_vien[ma_tim_kiem]
    print(f'Thông tin nhân viên: Mã: {ma_tim_kiem}, Tên: {thong_tin['ho_ten']}, Năm sinh: {thong_tin['nam_sinh']}, Lương: {thong_tin['luong']}')
else:
    print('Không tìm thấy nhân viên với mã này.')
#d
ma_tang_luong = input('Nhập mã nhân viên để tăng lương: ')
if ma_tang_luong in nhan_vien:
    nhan_vien[ma_tang_luong]['luong'] += 1000000
    print(f'Lương của nhân viên {ma_tang_luong} đã được tăng lên: {nhan_vien[ma_tang_luong]['luong']}')
else:
    print('Không tìm thấy nhân viên với mã này')
#e
ma_xoa = input('Nhập mã nhân viên để xóa: ')
if ma_xoa in nhan_vien:
    del nhan_vien[ma_xoa]
    print(f'Nhân viên với mã {ma_xoa} đã được xóa')
else:
    print('Không tìm thấy nhân viên với mã nà')
#f
danh_sach_nhan_vien = sorted(nhan_vien.items(), key=lambda x: x[1]['nam_sinh'], reverse=True)

print('Danh sách nhân viên sau khi sắp xếp theo năm sinh giảm dần:')
for ma_nhan_vien, thong_tin in danh_sach_nhan_vien:
    print(f'Mã: {ma_nhan_vien}, Tên: {thong_tin['ho_ten']}, Năm sinh: {thong_tin['nam_sinh']}, Lương: {thong_tin['luong']}')