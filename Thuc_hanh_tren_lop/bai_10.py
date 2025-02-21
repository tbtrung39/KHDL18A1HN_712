start_hour = int(input("Nhập giờ bắt đầu (5-22): "))
end_hour = int(input("Nhập giờ kết thúc (5-22): "))

if start_hour < 5 or end_hour > 22 or start_hour >= end_hour:
    print("Giờ không hợp lệ!")
else:
    total_hours = end_hour - start_hour
    if total_hours <= 3:
        cost = total_hours * 100000
    else:
        cost = 3 * 100000 + (total_hours - 3) * 75000
    
    if 11 <= start_hour <= 15:
        cost *= 0.9  # Giảm 10%

    print(f"Tổng tiền thuê sân: {cost} đồng")
    