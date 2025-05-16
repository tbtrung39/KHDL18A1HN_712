from datetime import datetime

def main():
    try:
        ngay_nhap = input("Nhập ngày (dd-mm-yyyy): ")
        ngay = datetime.strptime(ngay_nhap, "%d-%m-%Y")
        thu_trong_tuan = ngay.weekday()

        thu_dict = {
            0: "Thứ Hai",
            1: "Thứ Ba",
            2: "Thứ Tư",
            3: "Thứ Năm",
            4: "Thứ Sáu",
            5: "Thứ Bảy",
            6: "Chủ Nhật"
        }

        print(f"Ngày {ngay.strftime('%d-%m-%Y')} là {thu_dict[thu_trong_tuan]}.")

    except ValueError:
        print("Lỗi: Định dạng ngày không hợp lệ. Vui lòng nhập theo dd-mm-yyyy.")

if __name__ == "__main__":
    main()
