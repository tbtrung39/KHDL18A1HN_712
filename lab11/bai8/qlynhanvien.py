from libs import xu_ly_thong_tin_nhanvien as xl

def main():
    print(" CHƯƠNG TRÌNH QUẢN LÝ NHÂN VIÊN ")
    ds = xl.nhap_danh_sach()
    ds = sorted(ds, key=lambda x: x["ThucLinh"], reverse=True)
    xl.hien_thi_danh_sach(ds)
    xl.luu_vao_csv(ds)

main()