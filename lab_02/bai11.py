days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month = int(input("Nhập tháng (1-12): "))
day = int(input("Nhập ngày (1-31): "))

if month < 1 or month > 12:
    print("Tháng không hợp lệ!")
elif day < 1 or day > days_in_month[month - 1]:
    print("Ngày không hợp lệ trong tháng!")
else:
    day += 1

    if day > days_in_month[month - 1]:
        day = 1  
        month += 1  
        if month > 12:
            month = 1

    print(f"Ngày tiếp theo là: {day}/{month}")
