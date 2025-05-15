import qlyhanghoa

danh_sach = qlyhanghoa.nhap_danh_sach()

print("\nDanh sách mặt hàng trước khi sắp xếp:")
qlyhanghoa.in_danh_sach(danh_sach)

print("\nDanh sách sau khi sắp xếp giảm dần theo Thuế:")
danh_sach_sx = qlyhanghoa.sap_xep_theo_thue(danh_sach)
qlyhanghoa.in_danh_sach(danh_sach_sx)
