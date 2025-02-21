days = {1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 
        5: "Thursday", 6: "Friday", 7: "Saturday"}

while True:
    day = int(input("Nhập thứ (1-7): "))
    if 1 <= day <= 7:
        print(f"Thứ {day} là {days[day]}")
        break
    print("Thứ không hợp lệ, vui lòng nhập lại!")