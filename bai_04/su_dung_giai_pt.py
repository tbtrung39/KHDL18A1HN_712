# su_dung_giai_pt.py

import giai_phuong_trinh

print("--- CHƯƠNG TRÌNH GIẢI PHƯƠNG TRÌNH ---")

while True:
    loai_pt = input("Chọn loại phương trình (1: bậc nhất, 2: bậc hai, 0: thoát): ")
    if loai_pt == '1':
        try:
            a = float(input("Nhập hệ số a: "))
            b = float(input("Nhập hệ số b: "))
            ket_qua = giai_phuong_trinh.giai_phuong_trinh_bac_nhat(a, b)
            print(f"Nghiệm của phương trình là: {ket_qua}")
        except ValueError:
            print("Vui lòng nhập số hợp lệ.")
    elif loai_pt == '2':
        try:
            a = float(input("Nhập hệ số a: "))
            b = float(input("Nhập hệ số b: "))
            c = float(input("Nhập hệ số c: "))
            ket_qua = giai_phuong_trinh.giai_phuong_trinh_bac_hai(a, b, c)
            print(f"Kết quả của phương trình là: {ket_qua}")
        except ValueError:
            print("Vui lòng nhập số hợp lệ.")
    elif loai_pt == '0':
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ.")