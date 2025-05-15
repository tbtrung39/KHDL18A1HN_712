from datetime import datetime

def tinh_khoang_cach(date1, date2):
    if date1 > date2:
        date1, date2 = date2, date1

    y1, m1, d1 = date1.year, date1.month, date1.day
    y2, m2, d2 = date2.year, date2.month, date2.day

    year_diff = y2 - y1
    month_diff = m2 - m1
    day_diff = d2 - d1

    if day_diff < 0:
        month_diff -= 1
        prev_month = m2 - 1 if m2 > 1 else 12
        prev_year = y2 if m2 > 1 else y2 - 1
        day_diff += (datetime(prev_year, prev_month % 12 + 1, 1) - datetime(prev_year, prev_month, 1)).days
    if month_diff < 0:
        month_diff += 12
        year_diff -= 1

    return year_diff, month_diff, day_diff

try:
    d1 = input("Nhập ngày thứ nhất (dd-mm-yyyy): ")
    d2 = input("Nhập ngày thứ hai (dd-mm-yyyy): ")

    date1 = datetime.strptime(d1, "%d-%m-%Y")
    date2 = datetime.strptime(d2, "%d-%m-%Y")

    y, m, d = tinh_khoang_cach(date1, date2)
    print(f"Hai ngày cách nhau: {y} năm, {m} tháng, {d} ngày")
except Exception as e:
    print("Lỗi:", e)
