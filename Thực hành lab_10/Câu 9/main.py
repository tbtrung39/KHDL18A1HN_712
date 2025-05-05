# main.py

import qlyhanghoa

def main():
    ds = qlyhanghoa.nhap_danh_sach()

    qlyhanghoa.in_danh_sach(ds, title="Trước khi sắp xếp theo Thuế VAT")
 
    ds_sorted = qlyhanghoa.sap_xep_giam_theo_thue(ds)

    qlyhanghoa.in_danh_sach(ds_sorted, title="Sau khi sắp xếp giảm dần theo Thuế VAT")

