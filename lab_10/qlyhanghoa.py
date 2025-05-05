def nhap_mat_hang():
    ma_hang = input("Nhập mã hàng (4 ký tự): ")
    ten_hang = input("Nhập tên hàng: ")
    don_vi = input("Nhập đơn vị tính: ")
    don_gia = float(input("Nhập đơn giá: "))
    so_luong = int(input("Nhập số lượng: "))
    thanh_tien = don_gia * so_luong
    thue = thanh_tien * 0.1

    return {
        "ma_hang": ma_hang,
        "ten_hang": ten_hang,
        "don_vi": don_vi,
        "don_gia": don_gia,
        "so_luong": so_luong,
        "thanh_tien": thanh_tien,
        "thue": thue
    }

def nhap_danh_sach():
    ds = []
    n = int(input("Nhập số lượng mặt hàng: "))
    for i in range(n):
        print(f"\nNhập mặt hàng thứ {i+1}:")
        ds.append(nhap_mat_hang())
    return ds

def hien_thi_danh_sach(ds):
    print("{:<8} {:<15} {:<10} {:<10} {:<10} {:<12} {:<10}".format(
        "Mã", "Tên hàng", "Đơn vị", "Đơn giá", "Số lượng", "Thành tiền", "Thuế"))
    for hang in ds:
        print("{:<8} {:<15} {:<10} {:<10.2f} {:<10} {:<12.2f} {:<10.2f}".format(
            hang["ma_hang"], hang["ten_hang"], hang["don_vi"], hang["don_gia"],
            hang["so_luong"], hang["thanh_tien"], hang["thue"]
        ))

def sap_xep_theo_thue(ds):
    return sorted(ds, key=lambda x: x["thue"], reverse=True)