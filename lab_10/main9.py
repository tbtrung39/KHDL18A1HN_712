import qlyhanghoa
danh_sach = qlyhanghoa.nhap_danh_sach()

print("--- Danh sách mặt hàng ban đầu ---")
qlyhanghoa.hien_thi_danh_sach(danh_sach)
danh_sach_sap_xep = qlyhanghoa.sap_xep_theo_thue(danh_sach)

print("--- Danh sách sau khi sắp xếp theo thuế giảm dần ---")
qlyhanghoa.hien_thi_danh_sach(danh_sach_sap_xep)