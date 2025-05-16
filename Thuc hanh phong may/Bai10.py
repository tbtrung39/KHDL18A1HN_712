from datetime import datetime
def main():
    try:
        d1 = input("Nhập ngày thứ nhất (dd-mm-yyyy): ")
        d2 = input("Nhập ngày thứ hai (dd-mm-yyyy): ")
        date1 = datetime.strptime(d1, "%d-%m-%Y")
        date2 = datetime.strptime(d2, "%d-%m-%Y")
        if date1 > date2:
            date1, date2 = date2, date1
        total_days = (date2 - date1).days

        years = total_days // 365
        months = (total_days % 365) // 30
        days = (total_days % 365) % 30

        print(f"Hai ngày cách nhau: {years} năm, {months} tháng, {days} ngày.")

    except ValueError:
        print("Lỗi: Định dạng ngày không hợp lệ. Dùng dd-mm-yyyy.")

if __name__ == "__main__":
    main()
