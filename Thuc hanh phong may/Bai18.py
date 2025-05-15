thí_sinh = {}
n = int(input("Nhập số lượng thí sinh ban đầu (0 nếu không có): "))
for _ in range(n):
    so_bao_danh = input("Nhập số báo danh: ")
    ho_ten = input("Nhập họ và tên: ")
    while True:
        try:
            diem_thi = float(input("Nhập điểm thi: "))
            diem_thi = round(diem_thi)
            if 0 <= diem_thi <= 10:
                break
            print("Điểm thi phải từ 0 đến 10! Vui lòng nhập lại.")
        except ValueError:
            print("Điểm không hợp lệ! Vui lòng nhập lại.")
    thí_sinh[so_bao_danh] = {'ho_ten': ho_ten, 'diem_thi': diem_thi}
while True:
    so_bao_danh_tra_cuu = input("Nhập số báo danh để tra cứu (hoặc 'exit' để thoát): ")

    if so_bao_danh_tra_cuu.lower() == 'exit':
        break
    if so_bao_danh_tra_cuu in thí_sinh:
        info = thí_sinh[so_bao_danh_tra_cuu]
        print(f"Họ và tên: {info['ho_ten']}, Điểm thi: {info['diem_thi']}")
    else:
        # Nếu không tồn tại, bổ sung thông tin
        ho_ten = input("Nhập họ và tên cho số báo danh mới: ")
        while True:
            try:
                diem_thi = float(input("Nhập điểm thi: "))
                diem_thi = round(diem_thi)
                if 0 <= diem_thi <= 10:
                    break
                print("Điểm thi phải từ 0 đến 10! Vui lòng nhập lại.")
            except ValueError:
                print("Điểm không hợp lệ! Vui lòng nhập lại.")
        thí_sinh[so_bao_danh_tra_cuu] = {'ho_ten': ho_ten, 'diem_thi': diem_thi}
        print("Đã bổ sung thông tin thí sinh vào từ điển.")
print("\nToàn bộ thông tin thí sinh:", thí_sinh)