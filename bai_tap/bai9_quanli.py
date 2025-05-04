ds_hanghoa = []
def nhap_mat_hang():
    ma = input("Nhập mã hàng: ")
    ten = input("Nhập tên hàng: ")
    don_vi = input("Nhập đơn vị tính: ")
    don_gia = float(input("Nhập đơn giá: "))
    so_luong = int(input("Nhập số lượng: "))
    hang = {
        'ma': ma,
        'ten': ten,
        'don_vi': don_vi,
        'don_gia': don_gia,
        'so_luong': so_luong
    }
    ds_hanghoa.append(hang)

def tinh_thanh_tien(hang):
    return hang['don_gia'] * hang['so_luong']

def tinh_thue(hang):
    return tinh_thanh_tien(hang) * 0.1

def xuat_danh_sach():
    for hang in ds_hanghoa:
        tt = tinh_thanh_tien(hang)
        thue = tinh_thue(hang)
        print(f"{hang['ma']} - {hang['ten']} - {hang['don_vi']} - {hang['don_gia']} - {hang['so_luong']} - Thành tiền: {tt} - Thuế: {thue}")

def sap_xep_theo_thue():
    ds_hanghoa.sort(key=lambda h: tinh_thue(h), reverse=True)
