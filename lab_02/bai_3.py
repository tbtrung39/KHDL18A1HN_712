def tim_thu(t):
    thu = {
        1: "Sunday", 2: "Monday", 3: "Tuesday",
        4: "Wednesday", 5: "Thursday", 6: "Friday", 7: "Saturday"
    }
    return thu.get(t, "Thứ không hợp lệ")

while True:
    thu = int(input("Nhập thứ trong tuần (1-7): "))
    if 1 <= thu <= 7:
        break
    print("Thứ nhập vào không hợp lệ, vui lòng nhập lại.")
print(f"Thứ đã nhập có tên là: {tim_thu(thu)}")
