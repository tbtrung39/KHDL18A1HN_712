danh_sach_sv = {}
n = int(input("Nhập số lượng sinh viên: "))
for _ in range(n):
    while True:
        ma_sv = input("Nhập mã sinh viên (6 ký tự số): ")
        if ma_sv.isdigit() and len(ma_sv) == 6:
            break
        print("Mã sinh viên không hợp lệ! Vui lòng nhập lại (6 ký tự số).")
    ten_sv = input("Nhập tên sinh viên: ")
    while True:
        try:
            diem = float(input("Nhập điểm số: "))
            diem = round(diem)
            if 0 <= diem <= 10:
                break
            print("Điểm số phải từ 0 đến 10! Vui lòng nhập lại.")
        except ValueError:
            print("Điểm không hợp lệ! Vui lòng nhập lại.")
    danh_sach_sv[ma_sv] = {'ten': ten_sv, 'diem': diem}
sorted_sv = sorted(danh_sach_sv.items(), key=lambda x: x[1]['diem'], reverse=True)
print("\nDanh sách sinh viên theo điểm giảm dần:")
print("Mã SV\tTên Sinh Viên\tĐiểm")
for ma_sv, info in sorted_sv:
    print(f"{ma_sv}\t{info['ten']}\t\t{info['diem']}")