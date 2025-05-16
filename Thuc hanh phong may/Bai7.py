from datetime import datetime, timedelta
def main():
    try:
        ngay_nhap = input("Nhập ngày (dd-mm-yyyy): ")
        ngay_hien_tai = datetime.strptime(ngay_nhap, "%d-%m-%Y")
        ngay_ke_tiep = ngay_hien_tai + timedelta(days=1)
        
        print("Ngày kế tiếp là:", ngay_ke_tiep.strftime("%d-%m-%Y"))

    except ValueError:
        print("Lỗi: Ngày nhập không hợp lệ. Định dạng đúng là dd-mm-yyyy.")

if __name__ == "__main__":
    main()
