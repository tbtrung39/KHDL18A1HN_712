class MatHang:
    def __init__(self, ma_hang, ten_hang, don_vi_tinh, don_gia, so_luong):
        self.ma_hang = ma_hang
        self.ten_hang = ten_hang
        self.don_vi_tinh = don_vi_tinh
        self.don_gia = don_gia
        self.so_luong = so_luong
        self.thanh_tien = self.tinh_thanh_tien()
        self.thue = self.tinh_thue()

    def tinh_thanh_tien(self):
        return self.don_gia * self.so_luong

    def tinh_thue(self):
        return self.thanh_tien * 0.1

    def __str__(self):
        return (f"{self.ma_hang:10} {self.ten_hang:15} {self.don_vi_tinh:10} "
                f"{self.don_gia:<10} {self.so_luong:<10} {self.thanh_tien:<12} {self.thue:<10}")
