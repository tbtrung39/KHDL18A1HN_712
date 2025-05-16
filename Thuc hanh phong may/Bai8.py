from datetime import datetime, timedelta

def main():
    try:
        ngay_nhap = input("Nhập ngày (dd-mm-yyyy): ")
        ngay_hien_tai = datetime.strptime(ngay_nhap, "%d-%m-%Y")

        # Trừ đi 1 ngày
        ngay_truoc_do = ngay_hien_tai - timedelta(days=1)

        print("Ngày trước đó là:", ngay_truoc_do.strftime("%d-%m-%Y"))

    except ValueError:
        print("Lỗi: Ngày nhập không hợp lệ. Vui lòng nhập theo định dạng dd-mm-yyyy.")

if __name__ == "__main__":
    main()
