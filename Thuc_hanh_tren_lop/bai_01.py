def days_in_month(month):
    days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 
            7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    return days.get(month, "Tháng không hợp lệ!")

month = int(input("Nhập tháng (1-12): "))
print(f"Tháng {month} có {days_in_month(month)} ngày.")