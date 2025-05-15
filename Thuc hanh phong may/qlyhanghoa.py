class MatHang:
    def __init__(self, ma, ten, donvi, dongia, soluong):
        self.ma = ma
        self.ten = ten
        self.donvi = donvi
        self.dongia = dongia
        self.soluong = soluong
        self.thanhtien = self.tinh_thanh_tien()
        self.thue = self.tinh_thue()

    def tinh_thanh_tien(self):
        return self.dongia * self.soluong

    def tinh_thue(self):
        return self.thanhtien * 0.10

    def __str__(self):
        return f"{self.ma:6} | {self.ten:15} | {self.donvi:10} | {self.dongia:7,.0f} | {self.soluong:7} | {self.thanhtien:10,.0f} | {self.thue:10,.0f}"

def nhap_danh_sach():
    ds = []
    n = int(input("Nhập số mặt hàng: "))
    for i in range(n):
        print(f"\nMặt hàng thứ {i+1}:")
        ma = input("Mã hàng (4 ký tự): ")
        ten = input("Tên hàng: ")
        donvi = input("Đơn vị tính: ")
        dongia = float(input("Đơn giá: "))
        soluong = int(input("Số lượng: "))
        ds.append(MatHang(ma, ten, donvi, dongia, soluong))
    return ds

def in_danh_sach(ds):
    print(f"{'Mã':6} | {'Tên hàng':15} | {'Đơn vị':10} | {'Đơn giá':7} | {'S.lượng':7} | {'Thành tiền':12} | {'Thuế':10}")
    print("-" * 90)
    for mh in ds:
        print(mh)

def sap_xep_theo_thue(ds):
    return sorted(ds, key=lambda x: x.thue, reverse=True)
