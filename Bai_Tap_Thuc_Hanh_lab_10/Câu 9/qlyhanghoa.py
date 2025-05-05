def nhap_mat_hang():

    mh = {}
    mh['ma_hang'] = input("Nhập mã hàng (4 ký tự): ")
    mh['ten_hang'] = input("Nhập tên hàng: ")
    mh['don_vi'] = input("Nhập đơn vị tính: ")
    mh['don_gia'] = float(input("Nhập đơn giá: "))
    mh['so_luong'] = int(input("Nhập số lượng: "))
    return mh

def tinh_thanh_tien(mh):
    mh['thanh_tien'] = mh['don_gia'] * mh['so_luong']

def tinh_thue_VAT(mh, ti_le=0.10):
    mh['thue_VAT'] = mh['thanh_tien'] * ti_le

def nhap_danh_sach():
    ds = []
    N = int(input("Nhập số lượng mặt hàng N: "))
    for i in range(N):
        print(f"\n--- Nhập thông tin mặt hàng thứ {i+1} ---")
        mh = nhap_mat_hang()
        tinh_thanh_tien(mh)
        tinh_thue_VAT(mh)
        ds.append(mh)
    return ds

def in_mat_hang(mh):
    print(f"{mh['ma_hang']:6} | {mh['ten_hang']:20} | {mh['don_vi']:8} | "
          f"{mh['don_gia']:10.2f} | {mh['so_luong']:8d} | "
          f"{mh['thanh_tien']:12.2f} | {mh['thue_VAT']:8.2f}")

def in_danh_sach(ds, title="Danh sách mặt hàng"):
    print(f"\n==== {title} ====")
    print("Mã    | Tên hàng            | Đơn vị   |   Đơn giá |  Số lượng | Thành tiền | Thuế VAT")
    print("-"*90)
    for mh in ds:
        in_mat_hang(mh)

def sap_xep_giam_theo_thue(ds):
    return sorted(ds, key=lambda mh: mh['thue_VAT'], reverse=True)