# su_dung_doicoso2.py

import doicoso2

print("--- CHƯƠNG TRÌNH XỬ LÝ CHUỖI SỐ VÀ ĐỔI CƠ SỐ ---")

while True:
    lua_chon = input("Chọn chức năng (1: Lọc chuỗi, 2: Xác định cơ số, 3: Đổi sang cơ số 10, 0: Thoát): ")
    if lua_chon == '1':
        chuoi_nhap = input("Nhập chuỗi ký tự: ")
        ket_qua = doicoso2.loai_bo_ky_tu_khong_hop_le(chuoi_nhap)
        print(f"Chuỗi sau khi lọc: {ket_qua}")
    elif lua_chon == '2':
        chuoi_nhap = input("Nhập chuỗi số: ")
        ket_qua = doicoso2.xac_dinh_co_so(chuoi_nhap)
        print(f"Chuỗi '{chuoi_nhap}' có thể là: {ket_qua}")
    elif lua_chon == '3':
        chuoi_nhap = input("Nhập chuỗi số: ")
        co_so_nhap = int(input("Nhập cơ số của chuỗi (2, 8 hoặc 16): "))
        ket_qua = doicoso2.sang_co_so_10(chuoi_nhap, co_so_nhap)
        print(f"Giá trị cơ số 10 của '{chuoi_nhap}' (cơ số {co_so_nhap}) là: {ket_qua}")
    elif lua_chon == '0':
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ.")