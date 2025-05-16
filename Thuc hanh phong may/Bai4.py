def sao_chep_tap_tin(ten_tap_tin_nguon, ten_tap_tin_dich):
    try:
        with open(ten_tap_tin_nguon, 'r', encoding='utf-8') as f_nguon:
            noi_dung = f_nguon.read()
        with open(ten_tap_tin_dich, 'w', encoding='utf-8') as f_dich:
            f_dich.write(noi_dung)

        print(f"Đã sao chép nội dung từ '{ten_tap_tin_nguon}' sang '{ten_tap_tin_dich}' thành công.")
    except FileNotFoundError:
        print("Lỗi: Không tìm thấy tập tin nguồn.")
    except IOError:
        print("Lỗi: Không thể đọc hoặc ghi tập tin.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
ten_tap_tin_nguon = input("Nhập tên tập tin nguồn: ")
ten_tap_tin_dich = input("Nhập tên tập tin đích: ")
sao_chep_tap_tin(ten_tap_tin_nguon, ten_tap_tin_dich)
